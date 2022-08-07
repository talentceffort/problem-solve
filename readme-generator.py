import os
import sys

folder_list = []
readme_list = []

for f in os.listdir(os.getcwd()):
    if os.path.isdir(f):
        folder_list.append(f)


if ".git" or "text" in folder_list:
    folder_list.pop(folder_list.index(".git"))
    folder_list.pop(folder_list.index("text"))

for d in folder_list:
    os.chdir(d)

    # 폴더 내 파일 목록 보기
    file_list = os.listdir(os.getcwd())

    dic = {}

    if not file_list:
        continue

    for f in file_list:
        file = f.split("_")

        if len(file) != 4:
            break

        problem_type = file[0]
        name = file[0] + "_" + file[1]
        trial_count = file[2]
        is_solved = "✅" if file[-1].split(".py")[0] == "O" else "❌"

        ##
        if name in dic:
            dic[name]["trial_result"].append(is_solved)
        else:
            dic[name] = {}
            dic[name]["trial_result"] = []
            dic[name]["trial_result"].append(is_solved)

        dic[name]["problem_type"] = problem_type
        dic[name]["name"] = name.split("_")[1]
        dic[name]["trial_count"] = len(dic[name]["trial_result"])

    os.chdir("../")

    readme_list += [
        "## " + d,
        "| 구분 | 유형 | 문제 | 1회 풀이 | 2회 풀이 | 3회 풀이 |",
        "| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |",
    ]

    for key in dic.keys():

        problem_solve_results = dic[key]["trial_result"]

        value = ["" for x in range(10)]

        for i in range(len(problem_solve_results)):
            value[i] = problem_solve_results[i]

        readme_list += [
            "| "
            + " | ".join(
                [
                    d,
                    dic[key]["problem_type"],
                    dic[key]["name"],
                    value[0],
                    value[1],
                    value[2],
                ]
            )
            + " |"
        ]


with open("README.md", "w") as f:
    for line in readme_list:
        f.write(line + "\n")
