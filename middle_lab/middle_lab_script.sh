#!/bin/bash


#pulling dockerui
echo -e "pulling middlelab...\n"
sudo docker pull tomratzon/new_image_name

choice=0
while [ $choice != "7" ]
do
        echo -e "\nchoose an action\n\n1) run container\n2) delete container\n3) stop container\n4) start container\n5) delete image\n6) create image\n7) exit\n"
        read choice
        if [ $choice == "1" ]
        then
                echo -e "choose name for container"
                read name
                sudo docker run -d -p 80 --name $name tomratzon/new_image_name
                echo -e "$name is up and running\n"

        elif [ $choice == "2" ]
        then
                echo -e "enter container name to delete: "
                read name
                sudo docker rm -f $name
                echo -e "$name is no more!\n"
       elif [ $choice == "3" ]
        then
                echo -e "enter container name to stop: "
                read name
                sudo docker stop $name
                echo -e "$name has stopped\n"

       elif [ $choice == "4" ]
        then
                echo -e "enter container name to start: "
                read name
                sudo docker start $name
                echo -e "$name hsas started!\n"


        elif [ $choice == "5" ]
        then
                echo -e "enter image id to delete: : "
                read id
 		sudo docker rmi $id
                echo -e "$id is no more!\n"

        elif [ $choice == "6" ]
        then
                echo -e "enter image name to create: "
                read name
                sudo docker build -t $name .
                echo -e "$name was created"
	elif [ $choice == "7" ]
	then
                echo -e "Exiting...\n"
        else
                echo -e "not a valid choice\n"
        fi
done


