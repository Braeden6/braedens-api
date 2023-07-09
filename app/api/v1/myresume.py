from fastapi import WebSocket, APIRouter, Depends, HTTPException





router = APIRouter()


@router.get("/myresume")
async def get_myresume():
    return {
    "name": "Braeden Norman",
    "email": "braeden.norman6@gmail.com",
    "phoneNumber": "778-668-9405",
    "Github": "https://github.com/Braeden6",
    "LinkedIn": "https://linkedin.com/in/braeden6",
    "titleFacts": ["Computer Science BSc", "Bilingual","Engineering/Software Engineering Work Experience"],
    "sections": [
        {
            "sectionTitle": "Technical Skills",
            "templateType": "TechSkillTemplate",
            "list": [
                { 
                    "title" : "Programming Languages",
                    "descriptor": "Python, TypeScript, JavaScript, Java, HTML, CSS",
                },{
                    "title" : "Technologies",
                    "descriptor": "Docker, Kubernetes, GCP, Azure, OpenAI, LangChain, GitHub" 
                }, {
                    "title" : "Framework",
                    "descriptor": "FastAPI, Node.js, React, MUI, Firebase, Next.js"
                }]
        },
        {
            "sectionTitle": "Personal Projects",
            "templateType": "BasicTemplate",
            "list": [
                    {
                        "title": "Personal Website",
                        "date": "Sep 2022 – Current",
                        "list": ["Made a personal website with my resume, resume builder, and a map viewer",
                            "Deployed through GitHub CI/CD workflows on Azure Web App in a docker container",
                            "Implemented a frontend app using React with Bootstrap for styling",
                            "Developed a Node.js/Express.js backend with a RESTful API for user verification (JWT), data manipulation, and display in a resume builder and map from a Cosmos NoSQL Database"],
                        "technologies":    [ "React, Bootstrap, Azure, CosmosDB, JavaScript, HTML, CSS, Node.js, Docker, CI/CD, GitHub, JSON/GeoJSON, NoSQL, RESTful API"] 

                    },
                    {
                        "title": "The Programming Lab",
                        "date": "Feb – Current",
                        "list": ["Designed an auto-deploy platform for web development learning, leveraging GKE, Docker containers, and microservices architecture",
                            "Developed a FastAPI microservice to automatically build repositories and deploy them to the cluster, streamlining the deployment process",
                            "Utilized an ingress to expose the path, ensuring seamless accessibility for users",
                            "Committed to open-source principles, making all components and documentation publicly available",
                             "Created detailed documentation to facilitate understanding, enabling users to learn from the project's structure and processes" ],
                        "technologies" : ["Google Cloud, Kubernetes, CI/CD, FastAPI, Python, Microservices, Docker, GitHub APIs"]
                    }, 
                    {
                        "title": "Convolution Neural Net (CNN) Recognition",
                        "date": "Feb - Apr 2021",
                        "list": ["Made a game recognition program to detect inputs and determine responses",
                            "Took screen images, converted them to 8-bit black and white, and ran it through a CNN to identify the highest probability of the best response",
                            "Used multiprocessing to complete tasks in parallel"],
                        "technologies" : ["Python, Scikit-learn, GitHub, PIL, Pandas, Multiprocessing"]
                    },
                    
                ]
        },
        {
            "sectionTitle": "Work Experience",
            "templateType": "BasicTemplate",
            "list": [
                {
                    "title": "Full Stack Software Engineer",
                    "subTitle": "HCL Tech",
                    "date": "May - Aug 2021",
                    "list": [
                        "Developed API and database structure for an internal web developer blog platform, utilizing Java Spring Boot and MySQL for efficient data management",
                        "Utilized Agile development and JIRA for effective collaboration and timely milestones",
                        "Implemented a FastAPI-based Python microservice for image cropping, integrating Google Image APIs and Google Cloud Storage via RESTful APIs",
                        "Developed and designed internal Generative AI tools for authoring website"
                    ]
                },
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
            "templateType": "BasicTemplate",
            "list": [
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
            "templateType": "BasicTemplate",
            "list": [
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