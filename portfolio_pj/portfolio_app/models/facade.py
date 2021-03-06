from project import *
from skill import *
from profile import *
from service import *
from hobby import *


class Facade:
    @staticmethod
    def getProjects():
        projects = [
            Project(
                name="Zingit",
                tag="zingit",
                description=
                "When it comes to connecting buyers and sellers online, whether locally or nationally, we are passionate about doing it right. At Zingit we believe many of the online marketplaces available today fall short on delivering a seamless and enjoyable experience, and that is why we have created an exciting and innovative solution.",
                client="New Zealand",
                roles="Developer",
                skills="Xamarin | Xamarin.iOS | ASP.NET Web API",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=zingit.ui.droid&hl=en",
                        Platform.ANDROID),
                    Link("https://itunes.apple.com/app/id991759517",
                         Platform.IOS),
                ],
                screenshots=0
                ),
            Project(
                name="Neatwork",
                tag="neatwork",
                description=
                "Neatwork Pro is designed for lawyers, certified/chartered accountants (i.e. CPA, CA, CMA, CGA), certified financial analysts (CFA) and students of these professions. With Neatwork, you are able to filter displayed profiles based on professional specifications. For example, if you are looking to only network and have lunch with lawyers, simply add the filter in your Settings page. Meals and one-on-one encounters are widely known for their efficiency in building relationships. Optimize your lunch and coffee breaks!",
                client="Canada",
                roles="Developer",
                skills=
                "iOS Native | Parse | Google Places API | Facebook SDK | Linkedin SDK | Google+ SDK",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.neatwork.neatworkpro&hl=en",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/neat-work/id1084915840?mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="Con info",
                tag="conifno",
                description=
                "The CON INFO* Serial Number Guide App allows you to determine the year model of Construction, Earthmoving, Mining and Logging Machinery and Equipment from over 400 manufacturers by simply entering the make, model and serial number.",
                client="New Zealand",
                roles="Techincal Leader",
                skills="Xamarin | Xamarin.iOS | SQLite | ASP.NET Web API",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.coninfoapp.droid&hl=en",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/au/app/con-info-serial-number-guide-for-heavymachinery/id1122500544?mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="MLQPLUS TRUSTED LEADER",
                tag="mlq",
                description=
                "A practical and interactive learning program designed to equip users with the skills and tools required for effective leadership. Access leadership content, resources and inspiration. Key features include: Learn: complete the Trusted Leader Program - 5 core modules designed by leadership experts covering a wide range of topics including foundations of effective leadership, coaching and communication, transactional leadership skills, transformational leadership skills and emotional intelligence. Interact: learn through a mix of bite-sized information, engaging visuals and interactive content to get the most of out each module. Access tools: access to worksheets, tip sheets and additional resources that can be downloaded right to your device or shared with others. Test your knowledge: track your progress through leadership quizzes and surveys.",
                client="Australia",
                roles="Developer",
                skills="iOS | Android | Mobile Offline | Subscription IAP",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.mlqplus.trustedleader",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/trusted-leader/id1087207561",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="PLAYER REPORT v2",
                tag="playerreport",
                description=
                "Coaches and scouts! Rate, compare and share soccer player's skills. Use with your team or when scouting or recruiting soccer players. You can compare and share your assessment of soccer players' skills through email with other coaches and scouts.",
                client="OPTIMYSports",
                roles="Developer",
                skills=
                "Xamarin | Xamarin.iOS | SQLite | Mobile Offline | Non-consumable IAP",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.optimysports.playerreport2&hl=vi",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/vn/app/player-report-v2/id1043400437?l=vi&mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="yukitomo",
                tag="yukitomo",
                description=
                "Skiers and snowboarders, have you ever experienced getting lost or losing your friends in the mountains? Yukitomo helps you to find and locate your friends in realtime. Never get lost !",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Google Maps API | Firebase Realtime Chat | Realtime Geocoding",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://itunes.apple.com/us/app/yukitomo/id1072053931?mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="Okadabooks",
                tag="okadabooks",
                description=
                "The mobile online bookstore & the marketplace for writer to publish their book onto. Mobile apps are focused on reading experience. System is optimized for high performance & allow publisher controls their books as well.",
                client="Okadabooks",
                roles="Technical Leader",
                skills="iOS Native | Swift | ePub Reader SDK | AES Encryption",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://www.microsoft.com/en-us/store/p/okadabooks/9wzdncrd2dzc",
                        Platform.WINDOWS),
                    Link(
                        "https://play.google.com/store/apps/details?id=com.okadabooks&hl=en",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/okada-books/id1161393771?mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="abakus",
                tag="abakus",
                description=
                "A pocket-based financial management tool which stored your personal income and tax expenses along with all the receipts and cost based expenses associated with every property you own, allowing you to see your estimated annual tax return and the financial position of your portfolio at any time throughout the year, at just the touch of a button.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "iOS Native | Offline Caching | Cross-platform subscription IAP",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.windorwilgainvestments.abakus",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/au/app/abakus/id1129055100?ls=1&mt=8",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="sim library",
                tag="sim",
                description=
                "Mobile apps facilitate Singapore Institute of Management on room book management, schedule management, loans & requests management, events management (Workshops | Talks | Activities). The apps connect to various end-points (RESTful | SOAP | Legacy) to utilize large set of data through on Single Sign-On securiy mechanism.",
                client="Singapore",
                roles="Technical Leader",
                skills="iOS Native | SOAP | SSO | Javascript | WordPress",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.sim.simlibrary",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/sim-library/id1140361058",
                        Platform.IOS),
                ],
                screenshots=8
                ),
            Project(
                name="ovvy",
                tag="ovvy",
                description=
                "Ovvy is the easiest way to find, compare and engage reliable Service Providers. Merchants can also showcase their skills effectively be notified of jobs they are interested in doing.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Chat | Socket.IO | Paypal Mobile SDK | Push Notification",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link(
                        "https://play.google.com/store/apps/details?id=com.app.ovvy",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/sg/app/ovvy-the-people-marketplace/id1196834481",
                        Platform.IOS),
                ],
                screenshots=9),
            Project(
                name="socialoop",
                tag="socialoop",
                description=
                "Social network apps connect people together, hosting activities, checkin, hobbies, or just update their mood. All in one.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "iOS Native | Chat | XMPP Framework | Google Maps SDK | Google Maps API | Push Notification",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    
                ],
                screenshots=9),
            Project(
                name="ATOMS",
                tag="atoms",
                description=
                "Are you looking for a way you can do more to help those in need? ATOMs is a modern way to spend time and money on other people. Thanks to this app, you can boost your own happiness by improving the lives of other human beings. Research shows this is much more effective than buying more things for yourself.",
                client="Singapore",
                roles="Technical Leader",
                skills=
                "ASP.NET Web API | Azure | SignalR | Android | iOS | AngularJS | Paypal SDK",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[
                    Link("http://atoms.sg", Platform.WEB),
                    Link(
                        "https://play.google.com/store/apps/details?id=com.alpsnetworks.atoms",
                        Platform.ANDROID),
                    Link(
                        "https://itunes.apple.com/us/app/atoms-sg/id1186676679",
                        Platform.IOS),
                ],
                screenshots=0),
            Project(
                name="Billby",
                tag="billby",
                description=
                "Billby is the world first pocket based bill payment platform, giving you greater control over paying and managing your bills.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "Android | iOS | Amazon | SendGrid Email SDK | QR | PHP/Laravel | MySql",
                length="4 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[Link("http://billby.com.au/", Platform.WEB)],
                screenshots=13
                ),
            Project(
                name="fitaccess",
                tag="fitaccess",
                description=
                "FitAccess connect clients and trainers to get more traning together instantly. You can be a client who want to be trained and get fit, also be a trainer to provide a class for others.  More than getting in shape, we are connnecting people. Get out of your room and do some training.",
                client="Australia",
                roles="Technical Leader",
                skills=
                "iOS Native | Amazon | Chat XMPP | Stripe SDK | Push Notification",
                length="6 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=10),
            Project(
                name="avb",
                tag="avb",
                description=
                "Searching for clubs/bars/restaurants around you. See who have checked in and getting around with them instantly.",
                client="New Zealand",
                roles="Scrum Master",
                skills=
                "iOS Native | RxSwift MVVM | Android Native | RxJava | ASP.NET Web API | Google Maps API | SignalR | RealmDB",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=0),
            Project(
                name="axcro",
                tag="axcro",
                description=
                "Escrow-based shopping platform to gain consumer confidence whe purchasing service packages that are provided in parts over a period. This product will also serve as an additional platform to increase the sales of service provider by providing an alternative payment guaranteed platform.",
                client="Singapore",
                roles="Scrum Master",
                skills=
                "iOS Native | Android Native | Google Maps API | Google Civic Information API | PHP/Laravel | MySql",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=0),
            Project(
                name="multiply",
                tag="multiply",
                description=
                "Voting and plege platform for everyone to join and share their own opinions about the election around the world.",
                client="United States",
                roles="Scrum Master",
                skills=
                "iOS Native | Google Maps API | Stripe | PHP/Laravel | MySql",
                length="3 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=9),
            Project(
                name="tacko",
                tag="tacko",
                description=
                "Love to travel, but want to make money with benefit ? Tacko gives you many chances to buy and sell your items with other peoples when you are travelling around.",
                client="Singapore",
                roles="Scrum Master",
                skills=
                "iOS Native | RxSwift MVVM | Google Maps API | Stripe | Paypal | PHP/Laravel | MySql",
                length="5 months",
                categories=[Category.WEB, Category.MOBILE],
                links=[],
                screenshots=0),
        ]
        return projects

    @staticmethod
    def getSkills():
        skills = [
            Skill(name="C#", percent="85%"),
            Skill(name="Swift", percent="90%"),
            Skill(name="Obj-C", percent="80%"),
            Skill(name="Python", percent="60%"),
        ]
        return skills

    @staticmethod
    def getProfiles():
        profiles = [
            Profile(
                "education",
                profileItems=[
                    ProfileItem(
                        time="2010-2015",
                        title=
                        "University of Information Technology - Vietnam National University HCMC",
                        subTitle="Bachelor of Engineering",
                        descriptions=[])
                ]),
            Profile(
                "certificates",
                profileItems=[
                    ProfileItem(
                        time="2011",
                        title=
                        "Microsoft Server 2008 System Administrator - MCITP-SA",
                        subTitle="Nhat Nghe Education JSC",
                        descriptions=[]),
                    ProfileItem(
                        time="2014",
                        title="Best Member of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2015",
                        title="Best Team Leader of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2016",
                        title="Most Active Support of the Year",
                        subTitle="Beesightsoft",
                        descriptions=[]),
                    ProfileItem(
                        time="2017",
                        title="PSM I | Professional Scrum Master I",
                        subTitle="Scrum.org",
                        descriptions=[
                            "Demonstrated a fundamental level of Scrum mastery, proving an understanding of Scrum as described in the Scrum Guide and the concepts of applying Scrum."
                        ]),
                    ProfileItem(
                        time="2017",
                        title="CSPO | CERTIFIED Scrum Product Owner",
                        subTitle="ScrumAlliance.org",
                        descriptions=[
                            "Learn the foundation of Scrum and the scope of the Certified Scrum Product Owner's role from the best minds in Scrum.",
                            "Demonstrate to employers and peers your attainment of core Scrum knowledge.",
                            "Expand your career opportunities by staying relevant and marketable across all industry sectors adopting Agile practices.",
                            "Engage with a community of recognized Scrum experts who are committed to continuous improvement."
                        ]),
                ]),
        Profile(
            "work experiences",
            profileItems=[
                ProfileItem(
                    time="Jun '14 - Present",
                    title="Beesightsoft",
                    subTitle="SCRUM Master | iOS Specialist | .NET Ninja",
                    descriptions=[
                        "- Started as a Junior Developer, work across 20+ outsource projects in Elance/Upwork and other clients",
                        "- Depth knowledgements on basic and advanced programming techniques: REST APIs, threading, memory management, DI, Clean Architecture ... ",
                        "- Leverage as an iOS Team Leader, training/coaching/mentoring team member from junior level ",
                        "- Growth and scale up team in both size and depth ",
                        "- Task management, planning the development path for team member ",
                        "- Join in technical R&D department to get ahead of new technoligies and applying/spreading across team: Functional Reactive Programming... ",
                        "- Collaborate to setup CI/CD pipelines ",
                        "- Being trained as a Scrum Master, get rid of old-fashioned Waterfall and shift to Agile to gain productivity"
                    ]),
                ProfileItem(
                    time="Aug '17 - Present",
                    title="Upwork",
                    subTitle="Professional Freelancer",
                    descriptions=[]),
            ]),
            Profile(
                "PROFESSIONAL SKILLS",
                profileItems=[
                    ProfileItem(
                        time="Database",
                        title="SQL Server, Postgresql, MySql, Sqlite, Realm",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="IDE & Tools",
                        title="Visual Studio, Xamarin Studio, XCode, Visual Studio Code, Sublime Text",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="VCS / DVCS",
                        title="SVN, Git Bash, Bitbucket | GitHub | GitLab, Git Flow | GitHub Flow | GitLab Flow, Git Submodule | Subtree",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="CI & Build Tools",
                        title="Jenkins | Code quality (swiftlint, PEP8) | xcodebuild (iOS), xctest (iOS)",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="ALM",
                        title="Atlassian JIRA, Atlassian Confluence, ChatOps (HipChat | Slack)",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Framework",
                        title="Xamarin | iOS (Objective-C/Swift) | RxSwift | ASP.NET (MVC/Web API/Core) | NodeJS",
                        subTitle="",
                        descriptions=[]
                    ),
                    ProfileItem(
                        time="Architecture",
                        title="OOP/SOLID/DRY | Design Patterns | IoC/Dependency Injection | MVC/MVP/MVVM/Clean Architecture | Functional Reactive Programming",
                        subTitle="",
                        descriptions=[]
                    ),
                ]
            )
            ]
        return profiles

    @staticmethod
    def getHobbies():
        hobbies = [
            Hobby(
                name="Reading",
                quote="'Books are a uniquely portable magic'",
                author="Stephen King, On Writing: A Memoir of the Craft",
                image="flaticon-open-book"),
            Hobby(
                name="Guitar",
                quote="'I like to be quiet and play guitar and just chill.'",
                author="Post Malone",
                image="flaticon-acoustic-guitar"),
            Hobby(
                name="Travelling",
                quote=
                "'The world is a book, and those who do not travel read only a page.'",
                author="Saint Augustine",
                image="flaticon-aeroplane"),
            Hobby(
                name="Swimming",
                quote=
                "'The man who is swimming against the stream knows the strength of it.'",
                author="Woodrow Wilson",
                image="flaticon-swimmer"),
            Hobby(
                name="Gym",
                quote="'No pain, no gain'",
                author="Ben Franklin",
                image="flaticon-weightlifting"),
            Hobby(
                name="Soccer",
                quote="'Soccer is a magical game'",
                author="David Beckham",
                image="flaticon-soccer-ball-variant")
        ]
        return hobbies

    @staticmethod
    def getServices():
        services = [
            Service(
                name="Agile Consultant",
                description=
                "Consult, coaching how to steer with Agile best practices, tools, processes: Scrum | Kanban | Scrumban | BDD | TDD | XP",
                image="flaticon-two-thin-arrows-forming-a-circle"),
            Service(
                name="DevOps Consultant",
                description=
                "Architect, design full pipeline of DevOps from ALM (JIRA | Git) through CI (Jenkins) to CD (Docker | Configuration Management)",
                image="flaticon-infinite-symbol"),
            Service(
                name="Software Development",
                description=
                "Building clean and robust application using various programming languages: Swift, Objective-C, .NET, Python",
                image="flaticon-computer"),
        ]
        return services