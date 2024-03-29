﻿#include<sys/types.h>
#include<sys/socket.h>

#include<netinet/in.h>

#define TIME_SERVER  "211.223.201.30"
#define TIME_PORT    5010

main(){
	int sock;
	struct sockaddr_in server;
	char buf[256];
	
	if ((sock = socket(AF_INET, SOCK_STREAM, 0))==-1)
		exit(1);

	server.sin_family = AF_INET;
	server.sin_addr.s_addr = htonl(inet_addr(TIME_SERVER)); /* htonl() 생략 여부 */
	server.sin_port = htons(TIME_PORT);

	if (connect(sock, (struct sockaddr *)&server, sizeof(server)))
		exit(1);

	if (recv(sock, buf, sizeof(buf), 0)==-1)
		exit(1);
	printf("Time information from server is %s", buf);
	close(sock);
}