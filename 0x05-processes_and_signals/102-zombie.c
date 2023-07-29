#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - pause
 *
 * Return: int
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
 * main - zombie
 *
 * Return: int
 */
int main(void)
{
	int i = 0;
	pid_t zid;

	for (i = 0; i < 5; i++)
	{
		zid = fork();
		if (zid)
			printf("Zombie process created, PID: %i\n", zid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
