
serial_implicito:
	python exampleImplicitSerial.py

serial_explicito:
	python exampleSerial.py
paralelo_implicito:

paralelo_explicito:
	mpiexec -n 40 -hostfile ./hostfile python ./exampleParallel.py
	
paralelo_explicito_un_nodo:
	mpiexec -n  4 python ./examples/exampleParallel.py
	
import_test:
	mpiexec -n 60 -hostfile ./hostfile python ./test/importTest.py
	
