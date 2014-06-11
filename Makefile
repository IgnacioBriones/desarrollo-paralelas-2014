
serial_implicito:
	python exampleSerial.py

serial_explicito:

paralelo_implicito:

paralelo_explicito:
	mpiexec -n 60 -hostfile ./hostfile python ./examples/exampleParallel.py