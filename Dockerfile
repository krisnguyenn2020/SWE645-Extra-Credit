# Base image
FROM openjdk:17-jdk

# Expose port for application
EXPOSE 8080

# Set arguement for jar file
ARG JAR_FILE=target/student-survey-0.0.1-SNAPSHOT.jar

# Copy to current directory 
COPY ${JAR_FILE} .

# Command to run application
CMD [ "java", "-jar",  "student-survey-0.0.1-SNAPSHOT.jar"]
