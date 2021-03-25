from qtpy import QtWidgets
from qtpy import QtCore

from quocs_pyqtinterface.gui.OptimizationBasicGui import OptimizationBasicGui
from quocs_pyqtinterface.logic.OptimizationBasic import OptimizationBasic
from quocs_optlib.communication.AllInOneCommunication import AllInOneCommunication
from quocs_optlib.tools.dynamicimport import dynamic_import
import time


class OptimizationLogic(QtCore.QObject, OptimizationBasic):

    def start_optimization(self, opti_comm_dict):
        optimization_dictionary = opti_comm_dict["optimization_dictionary"]
        figure_of_merit_dictionary = opti_comm_dict["figure_of_merit"]
        # Get the optimizer attribute
        fom_attribute = dynamic_import(
            attribute=figure_of_merit_dictionary.setdefault("opti_algorithm_attribute", None),
            module_name=figure_of_merit_dictionary.setdefault("python_module", None),
            class_name=figure_of_merit_dictionary.setdefault("python_class", None))
        interface_job_name = optimization_dictionary["optimization_client_name"]
        communication_obj = AllInOneCommunication(
            interface_job_name=interface_job_name, fom_obj=fom_attribute(args_dict=figure_of_merit_dictionary),
            handle_exit_obj=self.handle_exit_obj,
            comm_signals_list=[self.message_label_signal, self.fom_plot_signal, self.controls_update_signal])
        # Get the optimizer attribute
        optimizer_attribute = dynamic_import(
            attribute=optimization_dictionary.setdefault("opti_algorithm_attribute", None),
            module_name=optimization_dictionary.setdefault("opti_algorithm_module", None),
            class_name=optimization_dictionary.setdefault("opti_algorithm_class", None))
        print("The dictionary you used")
        optimizer_obj = optimizer_attribute(optimization_dict=optimization_dictionary,
                                            communication_obj=communication_obj)
        try:
            optimizer_obj.begin()
            optimizer_obj.run()
        except Exception as ex:
            print("Unhandled exception: {}".format(ex.args))
            print("something goes wrong")
        finally:
            optimizer_obj.end()
        self.message_label_signal.emit("The optimization is finished")
        self.is_running_signal.emit(False)


class OptimizationSuiteGui(QtWidgets.QMainWindow, OptimizationBasicGui):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.optimizationlogic = OptimizationLogic()

        # Handle Thread for the optimization
        self.thread_optimization = QtCore.QThread(self)
        self.optimizationlogic.moveToThread(self.thread_optimization)
        self.thread_optimization.start()

        self.handle_ui_elements()
        self._mw.closeEvent = self.closeEvent

    def closeEvent(self, event):
        # Send the signal to the handle exit obj
        print("I am closing the Main Window ...")
        self.stop_optimization_signal.emit(False)
        print("Emitted signal to stop the optimization")
        # Close the optimization thread
        self.thread_optimization.quit()
        print("I am quitting the optimization thread")
        while self.thread_optimization.isRunning():
            print("The thread is still running ...")
            time.sleep(0.05)
        print("The thread is closed.")
        print("Bye Bye QuOCS")
        event.accept()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = OptimizationSuiteGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
