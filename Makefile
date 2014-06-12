
serial_implicito:
	python exampleSerial.py

serial_explicito:

paralelo_implicito:

paralelo_explicito:
	mpiexec -n 4 -hostfile ./hostfile python ./examples/exampleParallel.py
	
paralelo_explicito_un_nodo:
	python ./examples/exampleParallel.py
	