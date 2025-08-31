<img height="50" align="right" src="https://raw.githubusercontent.com/fchavonet/fchavonet/refs/heads/main/assets/images/logo-holberton_school.webp" alt="Holberton School logo">

# API

## Table of contents

<details>
    <summary>
        CLICK TO ENLARGE 😇
    </summary>
    <a href="#description">Description</a>
    <br>
    <a href="#objectives">Objectives</a>
    <br>
    <a href="#requirements">Requirements</a>
    <br>
    <a href="#instructions">Instructions</a>
    <br>
    <a href="#tech-stack">Tech stack</a>
    <br>
    <a href="#files-description">Files description</a>
    <br>
    <a href="#installation_and_how_to_use">Installation and how to use</a>
    <br>
    <a href="#thanks">Thanks</a>
    <br>
    <a href="#authors">Authors</a>
</details>

## <span id="description">Description</span>

This project demonstrates how to consume a REST API to fetch employee TODO data and export it into multiple formats using Python.
<br>
It is intentionally kept simple and educational: clear scripts, clean I/O, and compliance with Holberton’s style guidelines.

## <span id="objectives">Objectives</span>

At the end of this project, I should be able to explain to anyone, **without the help of Google**:

- What Bash scripting should not be used for?
- What is an API?
- What is a REST API?
- What are microservices?
- What is the CSV format?
- What is the JSON format?
- Pythonic Package and module name style.
- Pythonic Class name style.
- Pythonic Variable name style.
- Pythonic Function name style.
- Pythonic Constant name style.
- Significance of CapWords or CamelCase in Python.

## <span id="requirements">Requirements</span>

- The first line of all your files should be exactly `#!/usr/bin/python3`.
- Libraries imported in your Python files must be organized in alphabetical order.
- All my files should end with a new line.
- The length of your files will be tested using `wc`.
- My code should use the `pycodestyle`.
- All my files must be executable.
- I must use `get` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary).
- My code should not be executed when imported (by using `if __name__ == "__main__":`).

## <span id="instructions">Instructions</span>

### Mandatory

<details>
    <summary>
        <b>0. Gather data from an API</b>
    </summary>
    <br>

Write a Python script that, using this `REST API`, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

- You must use `urllib` or `requests` module.
- The script must accept an integer as a parameter, which is the employee ID.
- The script must display on the standard output the employee TODO list progress in this exact format:
    - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`:
        - `EMPLOYEE_NAME`: name of the employee.
        - `NUMBER_OF_DONE_TASKS`: number of completed tasks.
        - `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks.
    - Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`).

Example:

```bash
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
sylvain@ubuntu$
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
sylvain@ubuntu$
```

#
**Repo:**
- GitHub repository: `holbertonschool-back-end`.
- Directory: `api`.
- File: `0-gather_data_from_an_API.py`.
<hr>
</details>

<details>
    <summary>
        <b>1. Export to CSV</b>
    </summary>
    <br>

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

- Records all tasks that are owned by this employee.
- Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`.
- File name must be: `USER_ID.csv`.

Example:

```bash
sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
"2","Ervin Howell","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Ervin Howell","True","distinctio vitae autem nihil ut molestias quo"
"2","Ervin Howell","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Ervin Howell","False","adipisci non ad dicta qui amet quaerat doloribus ea"
"2","Ervin Howell","True","voluptas quo tenetur perspiciatis explicabo natus"
"2","Ervin Howell","True","aliquam aut quasi"
"2","Ervin Howell","True","veritatis pariatur delectus"
"2","Ervin Howell","False","nesciunt totam sit blanditiis sit"
"2","Ervin Howell","False","laborum aut in quam"
"2","Ervin Howell","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
"2","Ervin Howell","False","repudiandae totam in est sint facere fuga"
"2","Ervin Howell","False","earum doloribus ea doloremque quis"
"2","Ervin Howell","False","sint sit aut vero"
"2","Ervin Howell","False","porro aut necessitatibus eaque distinctio"
"2","Ervin Howell","True","repellendus veritatis molestias dicta incidunt"
"2","Ervin Howell","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
"2","Ervin Howell","False","sunt cum tempora"
"2","Ervin Howell","False","totam quia non"
"2","Ervin Howell","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
"2","Ervin Howell","True","totam atque quo nesciunt"
sylvain@ubuntu$
```

#
**Repo:**
- GitHub repository: `holbertonschool-back-end`.
- Directory: `api`.
- File: `1-export_to_CSV.py`.
<hr>
</details>

<details>
    <summary>
        <b>2. Export to JSON</b>
    </summary>
    <br>

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- Records all tasks that are owned by this employee.
- Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`.
- File name must be: `USER_ID.json`.

Example:

```bash
sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$
```

#
**Repo:**
- GitHub repository: `holbertonschool-back-end`.
- Directory: `api`.
- File: `2-export_to_JSON.py`.
<hr>
</details>

<details>
    <summary>
        <b>3. Dictionary of list of dictionaries</b>
    </summary>
    <br>

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- Records all tasks from all employees.
- Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`.
- File name must be: `todo_all_employees.json`.

Example:

```bash
sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
sylvain@ubuntu$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false}, {"username": "Bret", "task": "fugiat veniam minus", "completed": false}, {"username": "Bret", "task": "et porro tempora", "completed": true}, {"username": "Bret", "task": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false}, {"username": "Bret", "task": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false}, {"username": "Bret", "task": "illo expedita consequatur quia in", "completed": false}, {"username": "Bret", "task": "quo adipisci enim quam ut ab", "completed": true}, {"username": "Bret", "task": "molestiae perspiciatis ipsa", "completed": false}, {"username": "Bret", "task": "illo est ratione doloremque quia maiores aut", "completed": true}, {"username": "Bret", "task": "vero rerum temporibus dolor", "completed": true}, {"username": "Bret", "task": "ipsa repellendus fugit nisi", "completed": true}, {"username": "Bret", "task": "et doloremque nulla", "completed": false}, {"username": "Bret", "task": "repellendus sunt dolores architecto voluptatum", "completed": true}, {"username": "Bret", "task": "ab voluptatum amet voluptas", "completed": true}, {"username": "Bret", "task": "accusamus eos facilis sint et aut voluptatem", "completed": true}, {"username": "Bret", "task": "quo laboriosam deleniti aut qui", "completed": true}, {"username": "Bret", "task": "dolorum est consequatur ea mollitia in culpa", "completed": false}, {"username": "Bret", "task": "molestiae ipsa aut voluptatibus pariatur dolor nihil", "completed": true}, {"username": "Bret", "task": "ullam nobis libero sapiente ad optio sint", "completed": true}], "2": [{"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false}, {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": true}, {"username": "Antonette", "task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false}, {"username": "Antonette", "task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false}, {"username": "Antonette", "task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true}, {"username": "Antonette", "task": "aliquam aut quasi", "completed": true}, {"username": "Antonette", "task": "veritatis pariatur delectus", "completed": true}, {"username": "Antonette", "task": "nesciunt totam sit blanditiis sit", "completed": false}, {"username": "Antonette", "task": "laborum aut in quam", "completed": false}, {"username": "Antonette", "task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true}, {"username": "Antonette", "task": "repudiandae totam in est sint facere fuga", "completed": false}, {"username": "Antonette", "task": "earum doloribus ea doloremque quis", "completed": false}, {"username": "Antonette", "task": "sint sit aut vero", "completed": false}, {"username": "Antonette", "task": "porro aut necessitatibus eaque distinctio", "completed": false}, {"username": "Antonette", "task": "repellendus veritatis molestias dicta incidunt", "completed": true}, {"username": "Antonette", "task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true}, {"username": "Antonette", "task": "sunt cum tempora", "completed": false}, {"username": "Antonette", "task": "totam quia non", "completed": false}, {"username": "Antonette", "task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false}, {"username": "Antonette", "task": "totam atque quo nesciunt", "completed": true}], "3": [{"username": "Samantha", "task": "aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit", "completed": false}, {"username": "Samantha", "task": "rerum perferendis error quia ut eveniet", "completed": false}, {"username": "Samantha", "task": "tempore ut sint quis recusandae", "completed": true}, {"username": "Samantha", "task": "cum debitis quis accusamus doloremque ipsa natus sapiente omnis", "completed": true}, {"username": "Samantha", "task": "velit soluta adipisci molestias reiciendis harum", "completed": false}, {"username": "Samantha", "task": "vel voluptatem repellat nihil placeat corporis", "completed": false}, {"username": "Samantha", "task": "nam qui rerum fugiat accusamus", "completed": false}, {"username": "Samantha", "task": "sit reprehenderit omnis quia", "completed": false}, {"username": "Samantha", "task": "ut necessitatibus aut maiores debitis officia blanditiis velit et", "completed": false}, {"username": "Samantha", "task": "cupiditate necessitatibus ullam aut quis dolor voluptate", "completed": true}, {"username": "Samantha", "task": "distinctio exercitationem ab doloribus", "completed": false}, {"username": "Samantha", "task": "nesciunt dolorum quis recusandae ad pariatur ratione", "completed": false}, {"username": "Samantha", "task": "qui labore est occaecati recusandae aliquid quam", "completed": false}, {"username": "Samantha", "task": "quis et est ut voluptate quam dolor", "completed": true}, {"username": "Samantha", "task": "voluptatum omnis minima qui occaecati provident nulla voluptatem ratione", "completed": true}, {"username": "Samantha", "task": "deleniti ea temporibus enim", "completed": true}, {"username": "Samantha", "task": "pariatur et magnam ea doloribus similique voluptatem rerum quia", "completed": false}, {"username": "Samantha", "task": "est dicta totam qui explicabo doloribus qui dignissimos", "completed": false}, {"username": "Samantha", "task": "perspiciatis velit id laborum placeat iusto et aliquam odio", "completed": false}, {"username": "Samantha", "task": "et sequi qui architecto ut adipisci", "completed": true}], "4": [{"username": "Karianne", "task": "odit optio omnis qui sunt", "completed": true}, {"username": "Karianne", "task": "et placeat et tempore aspernatur sint numquam", "completed": false}, {"username": "Karianne", "task": "doloremque aut dolores quidem fuga qui nulla", "completed": true}, {"username": "Karianne", "task": "voluptas consequatur qui ut quia magnam nemo esse", "completed": false}, {"username": "Karianne", "task": "fugiat pariatur ratione ut asperiores necessitatibus magni", "completed": false}, {"username": "Karianne", "task": "rerum eum molestias autem voluptatum sit optio", "completed": false}, {"username": "Karianne", "task": "quia voluptatibus voluptatem quos similique maiores repellat", "completed": false}, {"username": "Karianne", "task": "aut id perspiciatis voluptatem iusto", "completed": false}, {"username": "Karianne", "task": "doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit", "completed": false}, {"username": "Karianne", "task": "ut sequi accusantium et mollitia delectus sunt", "completed": false}, {"username": "Karianne", "task": "aut velit saepe ullam", "completed": false}, {"username": "Karianne", "task": "praesentium facilis facere quis harum voluptatibus voluptatem eum", "completed": false}, {"username": "Karianne", "task": "sint amet quia totam corporis qui exercitationem commodi", "completed": true}, {"username": "Karianne", "task": "expedita tempore nobis eveniet laborum maiores", "completed": false}, {"username": "Karianne", "task": "occaecati adipisci est possimus totam", "completed": false}, {"username": "Karianne", "task": "sequi dolorem sed", "completed": true}, {"username": "Karianne", "task": "maiores aut nesciunt delectus exercitationem vel assumenda eligendi at", "completed": false}, {"username": "Karianne", "task": "reiciendis est magnam amet nemo iste recusandae impedit quaerat", "completed": false}, {"username": "Karianne", "task": "eum ipsa maxime ut", "completed": true}, {"username": "Karianne", "task": "tempore molestias dolores rerum sequi voluptates ipsum consequatur", "completed": true}], "5": [{"username": "Kamren", "task": "suscipit qui totam", "completed": true}, {"username": "Kamren", "task": "voluptates eum voluptas et dicta", "completed": false}, {"username": "Kamren", "task": "quidem at rerum quis ex aut sit quam", "completed": true}, {"username": "Kamren", "task": "sunt veritatis ut voluptate", "completed": false}, {"username": "Kamren", "task": "et quia ad iste a", "completed": true}, {"username": "Kamren", "task": "incidunt ut saepe autem", "completed": true}, {"username": "Kamren", "task": "laudantium quae eligendi consequatur quia et vero autem", "completed": true}, {"username": "Kamren", "task": "vitae aut excepturi laboriosam sint aliquam et et accusantium", "completed": false}, {"username": "Kamren", "task": "sequi ut omnis et", "completed": true}, {"username": "Kamren", "task": "molestiae nisi accusantium tenetur dolorem et", "completed": true}, {"username": "Kamren", "task": "nulla quis consequatur saepe qui id expedita", "completed": true}, {"username": "Kamren", "task": "in omnis laboriosam", "completed": true}, {"username": "Kamren", "task": "odio iure consequatur molestiae quibusdam necessitatibus quia sint", "completed": true}, {"username": "Kamren", "task": "facilis modi saepe mollitia", "completed": false}, {"username": "Kamren", "task": "vel nihil et molestiae iusto assumenda nemo quo ut", "completed": true}, {"username": "Kamren", "task": "nobis suscipit ducimus enim asperiores voluptas", "completed": false}, {"username": "Kamren", "task": "dolorum laboriosam eos qui iure aliquam", "completed": false}, {"username": "Kamren", "task": "debitis accusantium ut quo facilis nihil quis sapiente necessitatibus", "completed": true}, {"username": "Kamren", "task": "neque voluptates ratione", "completed": false}, {"username": "Kamren", "task": "excepturi a et neque qui expedita vel voluptate", "completed": false}], "6": [{"username": "Leopoldo_Corkery", "task": "explicabo enim cumque porro aperiam occaecati minima", "completed": false}, {"username": "Leopoldo_Corkery", "task": "sed ab consequatur", "completed": false}, {"username": "Leopoldo_Corkery", "task": "non sunt delectus illo nulla tenetur enim omnis", "completed": false}, {"username": "Leopoldo_Corkery", "task": "excepturi non laudantium quo", "completed": false}, {"username": "Leopoldo_Corkery", "task": "totam quia dolorem et illum repellat voluptas optio", "completed": true}, {"username": "Leopoldo_Corkery", "task": "ad illo quis voluptatem temporibus", "completed": true}, {"username": "Leopoldo_Corkery", "task": "praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt", "completed": false}, {"username": "Leopoldo_Corkery", "task": "a eos eaque nihil et exercitationem incidunt delectus", "completed": true}, {"username": "Leopoldo_Corkery", "task": "autem temporibus harum quisquam in culpa", "completed": true}, {"username": "Leopoldo_Corkery", "task": "aut aut ea corporis", "completed": true}, {"username": "Leopoldo_Corkery", "task": "magni accusantium labore et id quis provident", "completed": false}, {"username": "Leopoldo_Corkery", "task": "consectetur impedit quisquam qui deserunt non rerum consequuntur eius", "completed": false}, {"username": "Leopoldo_Corkery", "task": "quia atque aliquam sunt impedit voluptatum rerum assumenda nisi", "completed": false}, {"username": "Leopoldo_Corkery", "task": "cupiditate quos possimus corporis quisquam exercitationem beatae", "completed": false}, {"username": "Leopoldo_Corkery", "task": "sed et ea eum", "completed": false}, {"username": "Leopoldo_Corkery", "task": "ipsa dolores vel facilis ut", "completed": true}, {"username": "Leopoldo_Corkery", "task": "sequi quae est et qui qui eveniet asperiores", "completed": false}, {"username": "Leopoldo_Corkery", "task": "quia modi consequatur vero fugiat", "completed": false}, {"username": "Leopoldo_Corkery", "task": "corporis ducimus ea perspiciatis iste", "completed": false}, {"username": "Leopoldo_Corkery", "task": "dolorem laboriosam vel voluptas et aliquam quasi", "completed": false}], "7": [{"username": "Elwyn.Skiles", "task": "inventore aut nihil minima laudantium hic qui omnis", "completed": true}, {"username": "Elwyn.Skiles", "task": "provident aut nobis culpa", "completed": true}, {"username": "Elwyn.Skiles", "task": "esse et quis iste est earum aut impedit", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui consectetur id", "completed": false}, {"username": "Elwyn.Skiles", "task": "aut quasi autem iste tempore illum possimus", "completed": false}, {"username": "Elwyn.Skiles", "task": "ut asperiores perspiciatis veniam ipsum rerum saepe", "completed": true}, {"username": "Elwyn.Skiles", "task": "voluptatem libero consectetur rerum ut", "completed": true}, {"username": "Elwyn.Skiles", "task": "eius omnis est qui voluptatem autem", "completed": false}, {"username": "Elwyn.Skiles", "task": "rerum culpa quis harum", "completed": false}, {"username": "Elwyn.Skiles", "task": "nulla aliquid eveniet harum laborum libero alias ut unde", "completed": true}, {"username": "Elwyn.Skiles", "task": "qui ea incidunt quis", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui molestiae voluptatibus velit iure harum quisquam", "completed": true}, {"username": "Elwyn.Skiles", "task": "et labore eos enim rerum consequatur sunt", "completed": true}, {"username": "Elwyn.Skiles", "task": "molestiae doloribus et laborum quod ea", "completed": false}, {"username": "Elwyn.Skiles", "task": "facere ipsa nam eum voluptates reiciendis vero qui", "completed": false}, {"username": "Elwyn.Skiles", "task": "asperiores illo tempora fuga sed ut quasi adipisci", "completed": false}, {"username": "Elwyn.Skiles", "task": "qui sit non", "completed": false}, {"username": "Elwyn.Skiles", "task": "placeat minima consequatur rem qui ut", "completed": true}, {"username": "Elwyn.Skiles", "task": "consequatur doloribus id possimus voluptas a voluptatem", "completed": false}, {"username": "Elwyn.Skiles", "task": "aut consectetur in blanditiis deserunt quia sed laboriosam", "completed": true}], "8": [{"username": "Maxime_Nienow", "task": "explicabo consectetur debitis voluptates quas quae culpa rerum non", "completed": true}, {"username": "Maxime_Nienow", "task": "maiores accusantium architecto necessitatibus reiciendis ea aut", "completed": true}, {"username": "Maxime_Nienow", "task": "eum non recusandae cupiditate animi", "completed": false}, {"username": "Maxime_Nienow", "task": "ut eum exercitationem sint", "completed": false}, {"username": "Maxime_Nienow", "task": "beatae qui ullam incidunt voluptatem non nisi aliquam", "completed": false}, {"username": "Maxime_Nienow", "task": "molestiae suscipit ratione nihil odio libero impedit vero totam", "completed": true}, {"username": "Maxime_Nienow", "task": "eum itaque quod reprehenderit et facilis dolor autem ut", "completed": true}, {"username": "Maxime_Nienow", "task": "esse quas et quo quasi exercitationem", "completed": false}, {"username": "Maxime_Nienow", "task": "animi voluptas quod perferendis est", "completed": false}, {"username": "Maxime_Nienow", "task": "eos amet tempore laudantium fugit a", "completed": false}, {"username": "Maxime_Nienow", "task": "accusamus adipisci dicta qui quo ea explicabo sed vero", "completed": true}, {"username": "Maxime_Nienow", "task": "odit eligendi recusandae doloremque cumque non", "completed": false}, {"username": "Maxime_Nienow", "task": "ea aperiam consequatur qui repellat eos", "completed": false}, {"username": "Maxime_Nienow", "task": "rerum non ex sapiente", "completed": true}, {"username": "Maxime_Nienow", "task": "voluptatem nobis consequatur et assumenda magnam", "completed": true}, {"username": "Maxime_Nienow", "task": "nam quia quia nulla repellat assumenda quibusdam sit nobis", "completed": true}, {"username": "Maxime_Nienow", "task": "dolorem veniam quisquam deserunt repellendus", "completed": true}, {"username": "Maxime_Nienow", "task": "debitis vitae delectus et harum accusamus aut deleniti a", "completed": true}, {"username": "Maxime_Nienow", "task": "debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis", "completed": true}, {"username": "Maxime_Nienow", "task": "et praesentium aliquam est", "completed": false}], "9": [{"username": "Delphine", "task": "ex hic consequuntur earum omnis alias ut occaecati culpa", "completed": true}, {"username": "Delphine", "task": "omnis laboriosam molestias animi sunt dolore", "completed": true}, {"username": "Delphine", "task": "natus corrupti maxime laudantium et voluptatem laboriosam odit", "completed": false}, {"username": "Delphine", "task": "reprehenderit quos aut aut consequatur est sed", "completed": false}, {"username": "Delphine", "task": "fugiat perferendis sed aut quidem", "completed": false}, {"username": "Delphine", "task": "quos quo possimus suscipit minima ut", "completed": false}, {"username": "Delphine", "task": "et quis minus quo a asperiores molestiae", "completed": false}, {"username": "Delphine", "task": "recusandae quia qui sunt libero", "completed": false}, {"username": "Delphine", "task": "ea odio perferendis officiis", "completed": true}, {"username": "Delphine", "task": "quisquam aliquam quia doloribus aut", "completed": false}, {"username": "Delphine", "task": "fugiat aut voluptatibus corrupti deleniti velit iste odio", "completed": true}, {"username": "Delphine", "task": "et provident amet rerum consectetur et voluptatum", "completed": false}, {"username": "Delphine", "task": "harum ad aperiam quis", "completed": false}, {"username": "Delphine", "task": "similique aut quo", "completed": false}, {"username": "Delphine", "task": "laudantium eius officia perferendis provident perspiciatis asperiores", "completed": true}, {"username": "Delphine", "task": "magni soluta corrupti ut maiores rem quidem", "completed": false}, {"username": "Delphine", "task": "et placeat temporibus voluptas est tempora quos quibusdam", "completed": false}, {"username": "Delphine", "task": "nesciunt itaque commodi tempore", "completed": true}, {"username": "Delphine", "task": "omnis consequuntur cupiditate impedit itaque ipsam quo", "completed": true}, {"username": "Delphine", "task": "debitis nisi et dolorem repellat et", "completed": true}], "10": [{"username": "Moriah.Stanton", "task": "ut cupiditate sequi aliquam fuga maiores", "completed": false}, {"username": "Moriah.Stanton", "task": "inventore saepe cumque et aut illum enim", "completed": true}, {"username": "Moriah.Stanton", "task": "omnis nulla eum aliquam distinctio", "completed": true}, {"username": "Moriah.Stanton", "task": "molestias modi perferendis perspiciatis", "completed": false}, {"username": "Moriah.Stanton", "task": "voluptates dignissimos sed doloribus animi quaerat aut", "completed": false}, {"username": "Moriah.Stanton", "task": "explicabo odio est et", "completed": false}, {"username": "Moriah.Stanton", "task": "consequuntur animi possimus", "completed": false}, {"username": "Moriah.Stanton", "task": "vel non beatae est", "completed": true}, {"username": "Moriah.Stanton", "task": "culpa eius et voluptatem et", "completed": true}, {"username": "Moriah.Stanton", "task": "accusamus sint iusto et voluptatem exercitationem", "completed": true}, {"username": "Moriah.Stanton", "task": "temporibus atque distinctio omnis eius impedit tempore molestias pariatur", "completed": true}, {"username": "Moriah.Stanton", "task": "ut quas possimus exercitationem sint voluptates", "completed": false}, {"username": "Moriah.Stanton", "task": "rerum debitis voluptatem qui eveniet tempora distinctio a", "completed": true}, {"username": "Moriah.Stanton", "task": "sed ut vero sit molestiae", "completed": false}, {"username": "Moriah.Stanton", "task": "rerum ex veniam mollitia voluptatibus pariatur", "completed": true}, {"username": "Moriah.Stanton", "task": "consequuntur aut ut fugit similique", "completed": true}, {"username": "Moriah.Stanton", "task": "dignissimos quo nobis earum saepe", "completed": true}, {"username": "Moriah.Stanton", "task": "quis eius est sint explicabo", "completed": true}, {"username": "Moriah.Stanton", "task": "numquam repellendus a magnam", "completed": true}, {"username": "Moriah.Stanton", "task": "ipsam aperiam voluptates qui", "completed": false}]}sylvain@ubuntu$
```

#
**Repo:**
- GitHub repository: `holbertonschool-back-end`.
- Directory: `api`.
- File: `3-dictionary_of_list_of_dictionaries.py`.
<hr>
</details>

## <span id="tech-stack">Tech stack</span>

<p align="left">
    <img src="https://img.shields.io/badge/PYTHON-3776ab?logo=python&logoColor=white&style=for-the-badge" alt="Python badge">
    <img src="https://img.shields.io/badge/CSV-2d572c?logo=files&logoColor=white&style=for-the-badge" alt="CSV badge">
    <img src="https://img.shields.io/badge/JSON-000000?logo=json&logoColor=white&style=for-the-badge" alt="JSON badge">
    <img src="https://img.shields.io/badge/GIT-f05032?logo=git&logoColor=white&style=for-the-badge" alt="Git badge">
    <img src="https://img.shields.io/badge/GITHUB-181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub badge">
    <img src="https://img.shields.io/badge/MARKDOWN-000000?logo=markdown&logoColor=white&style=for-the-badge" alt="Markdown badge">
    <img src="https://img.shields.io/badge/VS CODE-007acc?logo=data:image/svg+xml;base64,PCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KDTwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIFRyYW5zZm9ybWVkIGJ5OiBTVkcgUmVwbyBNaXhlciBUb29scyAtLT4KPHN2ZyBmaWxsPSIjZmZmZmZmIiB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9Ii0wLjUgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KDTxnIGlkPSJTVkdSZXBvX2JnQ2FycmllciIgc3Ryb2tlLXdpZHRoPSIwIi8+Cg08ZyBpZD0iU1ZHUmVwb190cmFjZXJDYXJyaWVyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KDTxnIGlkPSJTVkdSZXBvX2ljb25DYXJyaWVyIj4KDTxwYXRoIGQ9Im0xNy44NTggMjMuOTk4LTkuNzcxLTkuNDg0LTUuODY2IDQuNDY1LTIuMjIxLTEuMTE1di0xMS43MTlsMi4yMzQtMS4xMjEgNS44NyA0LjQ2OSA5Ljc0Ny05LjQ5MyA1LjU4NyAyLjIzOXYxOS41MzFsLTUuNTc5IDIuMjN6bS0uNTYzLTE2LjE4Ni01LjU3NyA0LjE3MyA1LjU4IDQuMjAyem0tMTQuNTA3IDEuNjg1djUuMDE2bDIuNzg3LTIuNTI1eiIvPgoNPC9nPgoNPC9zdmc+&logoColor=white&style=for-the-badge" alt="VS Code badge">
</p>

## <span id="files-description">Files description</span>

| **FILES**                                 | **DESCRIPTION**                                                       |
| :---------------------------------------: | --------------------------------------------------------------------- |
| `0-gather_data_from_an_API.py`            | Print an employee’s TODO progress summary to `stdout`.                |
| `1-export_to_CSV.py`                      | Export all tasks of an employee to a CSV file named `<USER_ID>.csv`.  |
| `2-export_to_JSON.py`                     | Export all tasks of an employee to a JSON file named `<USER_ID>.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Export all tasks of all employees to `todo_all_employees.json`        |
| `requirements.txt`                        | List of dependencies required for the script.                         |
| `README.md`                               | The README file you are currently reading 😉.                        |

## <span id="installation_and_how_to_use">Installation and how to use</span>

### Installation:

1. Clone this repository:
    - Open your preferred Terminal.
    - Navigate to the directory where you want to clone the repository.
    - Run the following command:

```bash
git clone https://github.com/fchavonet/holbertonschool-back-end.git
```

2. Open the repository you've just cloned.

3. Navigate to the `api`:

```bash
cd api
```

4. Create a virtual environment:

```bash
python3 -m venv venv
```

5. Activate the virtual environment:

```bash
source venv/bin/activate
```

6. Install dependencies:

```bash
pip install -r requirements.txt
```

### How to use:

1. The scripts accept an employee ID (integer) unless stated otherwise:

- Task 0 - console report:

```bash
./0-gather_data_from_an_API.py 2
```

- Task 1 - export to CSV:

```bash
./1-export_to_CSV.py 2
```

- Task 2 - export to JSON:

```bash
./2-export_to_JSON.py 2
```

- Task 3 - export all employees to JSON:

```bash
./3-dictionary_of_list_of_dictionaries.py
```

## <span id="thanks">Thanks</span>

- A big thank you to all my Holberton School peers for their help and support throughout this project.

## <span id="authors">Authors</span>

**Fabien CHAVONET**
- GitHub: [@fchavonet](https://github.com/fchavonet)
