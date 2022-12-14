#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#define TIME_SERVER "211.223.201.30"
#define TIME_PORT 5010

main() {
	int sock;
	struct sockaddr_in server, client;
	int server_len = sizeof(server);
	char buf[256];
	int buf_len;

	server.sin_family = AF_INET;
	server.sin_addr.s_addr = htonl(inet_addr(TIME_SERVER));
	server.sin_port = htons(TIME_PORT);
	
	if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1)
		exit(1);
	client.sin_family = AF_INET;
	client.sin_addr.s_addr = htonl(INADDR_ANY);
	client.sin_port = htons(0);
	if (bind(sock, (struct sockaddr *)&client, sizeof(client)) < 0)
		exit(1);

	buf[0] = '?'; buf[1] = '\0';
	buf_len = sendto(sock, buf, strlen(buf) + 1, 0,
		(struct sockaddr *)&server, server_len);
	if (buf_len < 0)
		exit(1);

	buf_len = recvfrom(sock, buf, 256, 0, (struct sockaddr *)0, (int *)0);
	if (buf_len < 0)
		exit(1);
	printf("Time information from server is %s", buf);
	close(sock);
 }