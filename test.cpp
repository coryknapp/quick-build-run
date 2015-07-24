//qbr echo this should print out 1 lines
//qbr echo 1
//nothing done on this line
//qbr echo 2

//qbr echo you should't see this, because a non-comment line exists in the code
//preceding it.

int main(int, char *[])
{
	//qbr echo you should't see this
	return 0;
}

//qbr echo you should't see this
