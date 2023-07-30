#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - just infinite function
 * Return: (0) success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main entry
 * Return: (0) success (1) failed
 */
int main(void)
{
	pid_t pid;
	int i;

	/* on that machine pid_t is int */
	/* on other may be unsigned so better check first */
	/* to check the failure */
	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			/* we are in the child */
			exit(0);
		}
		else if (pid > 1)
		{
			/* we are in the parent and fork succeeded */
			/* since parent doesn't wait() for child to be executed */
			/* then child process if even when finished it will become */
			/* zombie process */
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid < 0)
		{
			/* we are in the parent and fork failed */
			exit(-1);
		}
	}
	infinite_while();
	return (0);
}
