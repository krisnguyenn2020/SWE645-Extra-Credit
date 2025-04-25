# SWE645-Extra-Credit
## Amazon RDS MySQL Database Setup

This microservice application uses a MySQL database hosted on Amazon RDS for storing survey responses. Below are the steps used to create and configure the database:

### Step 1: Access AWS Academy Lab
- Logged into AWS Academy Lab.
- Launched the lab environment and accessed the AWS Console.

  ![alt text](images/1_.jpg)

### Step 2: Navigate to Amazon RDS
- **Log in to the AWS Console** through the Learner Lab environment (usually via a **"Start Lab"** button).
- Once the lab environment is running, click **"AWS"** or **"Open AWS Console"** — this takes us to the AWS Management Console.
- In the AWS Console, use the **Search bar** at the top.
- Type `RDS` and select **Amazon RDS** from the dropdown.
- This takes us to the **Amazon RDS Dashboard**, where we can manage and create databases.
  
  ![alt text](images/2_.jpg)
  
### Step 3: Create RDS MySQL Instance
- Navigated to **Amazon RDS** in the AWS Console.
- Clicked **"Create database"**.
- Selected:
  - Engine: **MySQL**
  - Template: **Free tier** or **Dev/Test**
  - DB instance identifier: `student-survey-db`
  - Master username: `admin`
  - Master password: `${DB_PASSWORD}`

    ![alt text](images/1_CreateDatabase.jpg)

    ![alt text](images/2_Engin.png)
  
    ![alt text](images/3_Template.png)

    ![alt text](images/4_Setting.png)
  
### Step 4: Enable Public Access
- Set **Public Access**: `Yes` during database creation.
- Used the **default VPC security group**.

  ![alt text](images/5_Public.png)

### Step 5: Configure Security Group
- Go to EC2 > Security Groups to open the Security Group settings page.

   ![alt text](images/6_Open.png)
  
- Edited **Inbound Rules** of the selected security group:
  - Added rule:
    - **Type**: MySQL/Aurora
    - **Port**: 3306
    - **Source**: `0.0.0.0/0` (temporarily allowed all IPs for development)
      
      ![alt text](images/7_Edit.png)

      ![alt text](images/8_Add.png)

      ![alt text](images/(2)9_Save.png)

### Step 6: Get the RDS Endpoint URL
- After the database is created, go back to the **Amazon RDS dashboard**.
- Click on your DB instance name (e.g., `student-survey-db`).
- Under the **Connectivity & security** tab.
- Copy the **Endpoint** value (e.g., `student-survey-db.cpo6pmgwxit1.us-east-1.rds.amazonaws.com`).
- This endpoint will be used in our Spring Boot `application.properties`.

  ![alt text](images/(2)10_Dash.png)

  ![alt text](images/(2)11_Endpoint.png)
  
### Step 7: Provide Connection Details
- Update `application.properties` by adding the following credentials:
  
  **MySQL RDS Database Config:**
  
  ```properties
  spring.datasource.url=jdbc:mysql://student-survey-db.cdlpji3ifxr9.us-east-1.rds.amazonaws.com:3306/student-survey-db?createDatabaseIfNotExist=true
  spring.datasource.username=admin
  spring.datasource.password=${DB_PASSWORD}
  ```
  **Hibernate settings:**
  
  ```properties
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.jpa.hibernate.ddl-auto=update
  spring.jpa.show-sql=true
  spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
  ```

> Note: RDS automatically creates the schema from the Spring Boot entity if `spring.jpa.hibernate.ddl-auto=update` is enabled.

### Result
The database is publicly accessible and ready to be integrated with the Spring Boot backend. This setup allows the application to store and retrieve student survey data in a centralized, cloud-based relational database.
