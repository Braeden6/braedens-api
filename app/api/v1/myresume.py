from fastapi import WebSocket, APIRouter, Depends, HTTPException





router = APIRouter()


@router.get("/myresume")
async def get_myresume():
    return {
    "name": "Braeden Norman",
    "email": "braeden.norman6@gmail.com",
    "phoneNumber": "778-668-9405",
    "GitHub": "https://github.com/Braeden6",
    "LinkedIn": "https://linkedin.com/in/braeden-norman-49665a157",
    "titleFacts": ["Computer Science BSc", "Bilingual","Engineering/Software Engineering Work Experience"],
    "sections": [
        {
            "sectionTitle": "Technical Skills",
            "templateFunction": "getTechSkillTemplate",
            "subsections": [
                { 
                    "title" : "Programming Languages",
                    "list": ["C", "C++", "Java", "TypeScript", "Python", "JavaScript", "HTML", "CSS",
                    "Visual Basic", "MATLAB", "R", "Julia", "JSX" ]
                },{
                    "title" : "Technologies",
                    "list": [ "IntelliJ", "Visual Studios", "Microsoft Office", "Azure", "Node.js",
                    "React", "Bootstrap", "Serverless Computing", "Cosmos DB" ] 
                }]
        },
        {
            "sectionTitle": "Personal Projects",
            "templateFunction": "getBasicTemplate",
            "subsections": [
                    {
                        "title": "Sudoku Solver",
                        "date": "Aug 2022 - Current",
                        "list": ["Made a Sudoku solver app, in which you can use multiple different algorithms to solve sudoku puzzles to test and compare process speed",
                            "Implemented solver with search tree, breadth-first search and depth-first search, and other heuristics to speed up process time",
                            "Created a GUI with pyside6 that displays step-by-step solutions and allows you to solve puzzles yourself"],
                        "technologies":    [ "Python", "Pyside6", "Pandas", "Numpy", "Github"] 

                    },
                    {
                        "title": "Convolution Neural Net (CNN) Recognition",
                        "date": "Feb - Apr 2021",
                        "list": ["Made a game recognition program to detect inputs and determine responses",
                            "Took screen images, converted them to 8-bit black and white, and ran it through a CNN to identify the highest probability of the best response",
                            "Used multiprocessing to complete tasks in parallel"],
                        "technologies" : ["Python", "Scikit-learn", "GitHub", "PIL", "Pandas", "Multiprocessing"]
                    },
                    {
                        "title": "Maze Game",
                        "date": "Mar - Apr 2020",
                        "list": ["Developed a game where a player moves around a randomly generated map to interface with items",
                            "Utilized a visual-based system to give maximum view distance (fog of war)",
                            "Created and displayed visuals with a GUI using JFrame utilizing a constant update timer for visual rendering",
                            "Used JUnit for Unit testing to build a more robust bug-free game" ],
                        "technologies" : ["GitHub", "Java", "JUnit", "IntelliJ", "Swing"]
                    }, 
                    {
                        "title": "Map Drawer",
                        "date": "Jan - Apr 2020",
                        "list": ["Created a display system synced over multiple computers using a Socket and Server",
                        "Displayed a map where a dedicated user could reveal or cover up portions of the map using a drawing tool",
                        "Included Swing GUI that has a tools menu such as changing from drawing and erasing along with selecting draw size "],
                        "technologies" : ["Java", "Socket", "IntelliJ"]
                    }
                ]
        },
        {
            "sectionTitle": "Work Experience",
            "templateFunction": "getBasicTemplate",
            "subsections": [
                    {
                        "title": "Software Engineer", 
                        "subTitle": "Voronoi Health Analytics Inc.",
                        "date": "May - Aug 2021",
                        "list": ["Programmed and helped design an application for an AI-assisted medical imaging software",
                            "Implemented pyradiomics in software app to take DICOM information and print results to a readable table",
                            "Participated in weekly project meetings with owners and other employees",
                            "Worked in a collaborative environment using GitLab for ticket management and version control",
                            "Implemented front-end of the application in both MATLAB and C++, with Qt"
                        ]
                    },
                    {
                            "title": "Engineering Student (3 terms)", 
                            "subTitle": "SysEne Consulting Inc.",
                            "date": "Apr 2018 - Aug 2020",
                            "list": [ "Support for engineering analysis of energy-saving projects for mining and oil & gas clients",
                            "Collection, review, and organization of data from clients",
                            "Analysis of energy calculation to identify energy savings opportunities",
                            "Included significant documentation and revision control to ensure calculations were aligned with agreed-upon system configuration and the most representative data",
                            "Helped write technical reports for clients and government contracts",
                            "Created summary presentations for project updates and findings",
                            "Required significant scheduling and reporting to ensure meeting strict deadlines"
                        ]
                    },
                    {
                        
                        "title": "Referee",
                        "subTitle": "North Vancouver Minor Hockey Association",
                        "date": "Sep 2012 - Jun 2016",
                        "list":["Team leading skills while working with other linesman/refs",
                            "Patience while dealing with frustrated coaches and parents in the stands",
                            "Quick decision-making skills that follow the rule requirements (error management)"
                        ]
                    }
            ]
        },
        {
            "sectionTitle": "Education",
            "templateFunction": "getBasicTemplate",
            "subsections": [
                {
                    "title": "The University of British Columbia",
                    "subTitle": "Bachelor of Science- BS, Computer Science",
                    "date": "Sep 2020 - Apr 2022",
                    "list": []
                },
                {
                    "title": "The University of British Columbia",
                    "subTitle": "Bachelor of Applied Science - B.A.Sc., Electrical and Electronics Engineering, 2nd and 3rd Year ",
                    "date": "Sep 2018 - Apr 2020",
                    "list": []
                },
                {
                    "title": "Capilano University",
                    "subTitle": "Engineer Transition Diploma, First Year Engineering",
                    "date": "Sep 2016 - Apr 2018",
                    "list": []
                }
            ]
        },
        {
            "sectionTitle": "Licenses & Certifications",
            "templateFunction": "getBasicTemplate",
            "subsections": [
                {
                    "title": "Machine Learning with Python: A Practical Introduction - IBM ",
                    "subTitle": "Credential ID d8efcd09c8fb43f5af86b02a11c2704e",
                    "date": "Issued Aug 2020",
                    "list": []
                }
            ]
        }
    ]
}