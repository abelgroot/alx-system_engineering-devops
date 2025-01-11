#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Runs an infinite loop with
 * a 1-second sleep in each iteration.
 * Return: Always 0
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
 * main - Creates 5 zombie processes and displays their PIDs.
 * Return: Always 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("Fork failed");
			return (1);
		}
		else if (pid == 0)
		{
			/* Child process exits immediately to become a zombie */
			exit(0);
		}
		else
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", pid);
		}
	}

	infinite_while();
	return (0);
}
