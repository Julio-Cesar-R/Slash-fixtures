import slash
import logbook
import sys

# slash.config.root.debug.enabled = False
slash.config.root.log.colorize = True
slash.config.root.tmux.use_panes = True

# logbook.StreamHandler(sys.stdout).push_application()


@slash.skipped("no reason")
def test_1():

    slash.logger.debug("JULIO ROSAS")
    slash.logger.info("JULIO ROSAS")
    slash.logger.warn("JULIO ROSAS")
    slash.logger.error("JULIO ROSAS")
    slash.logger.notice("JULIO ROSAS")
    slash.logger.critical("JULIO ROSAS")


@slash.skipped("no reason")
def test_2():
    slash.logger.debug("Prueba numero 2")


@slash.skipped("no reason")
def test_3():
    slash.logger.debug("Prueba numero 3")
    slash.logger.notice("JULIO ROSAS")
