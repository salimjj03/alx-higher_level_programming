#!/bin/bash
#displays the size of the body of the response
curl -so /dev/null -w "%{http_code}" $1
