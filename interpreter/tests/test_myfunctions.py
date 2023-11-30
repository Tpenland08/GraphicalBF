from GraphicalBF import myfunctions


def test_gbfexec():
    assert myfunctions.gbfExec(
        "+++[>+++<-].*", ""
    ) == 0