import cx_Freeze

executables = [cx_Freeze.Executable("RaceGame.py")]

cx_Freeze.setup(
    name="Game Title Here",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["racecar.png"]}},
    executables = executables

    )
