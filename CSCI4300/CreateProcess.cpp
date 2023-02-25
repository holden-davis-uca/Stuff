//Holden Davis - Lab 1
//9/16/22 - Fall 2022
//Dr. Sun - CSCI 4300 - CRN 22807

//Preprocessor directive to use basic console input/output commands
#include <stdio.h>
//Preprocessor directive to use Win32 API
#include <windows.h>

//Single function program - entry point!
int main(VOID)
{
	//Define STARTUPINFO and PROCESS_INFORMATION objects
	STARTUPINFO si;
	PROCESS_INFORMATION pi;

	//Allocate memory for STARTUPINFO and PROCESS_INFORMATION objects (arguments are the pointer to the ojbect and its size)
	ZeroMemory(&si, sizeof(si));
	ZeroMemory(&pi, sizeof(pi));

	//Define a wchar_t array called "process" to contain the name of the program to be executed
	wchar_t process[] = L"C:\\Emulators\\cemu_1.26.1\\Cemu.exe";

	//Test if CreateProcess() returned true (success) or false (failure)
	if (!CreateProcess(
		NULL,		//lpApplicationName of type LPCTSTR:					We don't want to run a custom .exe executable so we leave this NULL
		process,	//lpCommandLine of type LPTSTR:							We do want to run the Windows Terminal executable wt.exe, so we set this to the "process" variable
		NULL,		//lpProcessAttributes of type LPSECURITY_ATTRIBUTES:	We're not too concerned with the security of our process, so we leave this NULL
		NULL,		//lpThreadAttributes of type LPSECURITY_ATTRIBUTES:		We're not too concerned with the security of our thread either, so we leave this NULL
		FALSE,		//BInheritHandles of type BOOL:							We don't want our child process to inherit the handle of the parent process, so we set this to FALSE
		0,			//dwCreationFlags of type DWORD:						We don't need any special creation flags for our process as we are simply running an executable
		NULL,		//lpEnvironment of type LPVOID:							We don't want our program to run in a separate environment from the parent, so we leave this NULL
		NULL,		//lpCurrentDirectory of type LPCSTR:					We don't want our program to start in a different working directory from the parent, so we leave this NULL
		&si,		//lpStartupInfo of type LPSTARTUPINFO:					This is the pointer to our STARTUPINFO object that we defined and allocated memory for earlier
		&pi			//lpProcessInfo of type LPROCESS_INFORMATION:			This is the pointer to our PROCESS_INFORMATION object that we defined and allocated memory for earlier
	))
	{
		//Failed! Print error message and return -1 to main()
		fprintf(stderr, "Process creation failed!, returning -1");
		return -1;
	}

	//In this example, we assume we're performing our computations on a single-processor system, where only one process can run at a time and parent and child processed cannot run in parallel. Therefore, we wait for our child process (referenced by the process handle stored in our PROCESS_INFORMATION object)
	WaitForSingleObject(pi.hProcess, 10000);

	//Let the user know we're done!
	printf("Finished waiting for child process! (via WaitForSingleObject())\n\n");

	//Here, we would typically call this method to close both the handle for the process and the handle for the thread, but because we're using TerminateProcess, we only need to close the thread handle
	//CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);

	//Here, we finally terminate the process by referencing its handle and providing an exit code (0 because we finished successfully)
	TerminateProcess(pi.hProcess, 0);

	//Pause and wait for user input so we can see our console output to the screen
	system("PAUSE");

	//Return 0 to main; we're all done!
	return 0;
}