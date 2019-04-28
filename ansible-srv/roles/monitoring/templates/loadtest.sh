 #!/bin/bash
 
 for i in {1..10000}
 do
     echo "Sending 50 requests using thread $i" && time curl -s -X POST http://159.203.14.101/api/design/survey?[1-50] > /dev/null &
 done
 wait
