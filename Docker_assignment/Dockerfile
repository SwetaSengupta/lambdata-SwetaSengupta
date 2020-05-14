FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
#Get python dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install python3-pip curl -y && \
    pip3 install numpy  && \
    pip3 install -i https://test.pypi.org/simple/ lambdata-sweta-assign1 && \
    pip3 install pipenv
    
RUN pip3 install pandas

