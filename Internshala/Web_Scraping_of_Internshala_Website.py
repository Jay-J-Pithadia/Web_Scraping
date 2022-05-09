from bs4 import BeautifulSoup

import requests


category_ = """
                <option value=".net%20development">.NET Development</option>
                <option value="3d%20printing">3D Printing</option>
                <option value="accounts">Accounts</option>
                <option value="acting">Acting</option>
                <option value="aerospace">Aerospace Engineering</option>
                <option value="agriculture%20and%20food%20engineering">Agriculture &amp; Food Engineering</option>
                <option value="analytics">Analytics</option>
                <option value="anchoring">Anchoring</option>
                <option value="android%20app%20development">Android App Development</option>
                <option value="angular.js%20development">Angular.js Development</option>
                <option value="animation">Animation</option>
                <option value="architecture">Architecture</option>
                <option value="artificial%20intelligence%20(ai)">Artificial Intelligence (AI)</option>
                <option value="asp.net">ASP.NET Development</option>
                <option value="audio%20making%2Fediting">Audio Making/Editing</option>
                <option value="automobile%20engineering">Automobile Engineering</option>
                <option value="backend%20development">Backend Development</option>
                <option value="big%20data">Big Data</option>
                <option value="bioinformatics">Bioinformatics</option>
                <option value="biology">Biology</option>
                <option value="biotech">Biotechnology Engineering</option>
                <option value="blockchain%20development">Blockchain Development</option>
                <option value="blogging">Blogging</option>
                <option value="brand%20management">Brand Management</option>
                <option value="cad%20design">CAD Design</option>
                <option value="campus%20ambassador">Campus Ambassador</option>
                <option value="chartered%20accountancy%20(ca)">Chartered Accountancy (CA)</option>
                <option value="chemical">Chemical Engineering</option>
                <option value="chemistry">Chemistry</option>
                <option value="cinematography">Cinematography</option>
                <option value="civil">Civil Engineering</option>
                <option value="client%20servicing">Client Servicing</option>
                <option value="cloud%20computing">Cloud Computing</option>
                <option value="commerce">Commerce</option>
                <option value="company%20secretary%20(cs)">Company Secretary (CS)</option>
                <option value="computer%20science">Computer Science</option>
                <option value="computer%20vision">Computer Vision</option>
                <option value="content%20writing">Content Writing</option>
                <option value="copywriting">Copywriting</option>
                <option value="creative%20writing">Creative Writing</option>
                <option value="culinary%20arts">Culinary Arts</option>
                <option value="customer%20service">Customer Service</option>
                <option value="cyber%20security">Cyber Security</option>
                <option value="data%20entry">Data Entry</option>
                <option value="data%20science">Data Science</option>
                <option value="database%20building">Database Building</option>
                <option value="design">Design</option>
                <option value="dietetics%2Fnutrition">Dietetics/Nutrition</option>
                <option value="digital%20marketing">Digital Marketing</option>
                <option value="editorial">Editorial</option>
                <option value="electrical">Electrical Engineering</option>
                <option value="electronics">Electronics Engineering</option>
                <option value="embedded%20systems">Embedded Systems</option>
                <option value="energy%20science%20and%20engineering">Energy Science &amp; Engineering</option>
                <option value="engineering">Engineering</option>
                <option value="engineering%20design">Engineering Design</option>
                <option value="engineering%20physics">Engineering Physics</option>
                <option value="environmental%20sciences">Environmental Sciences</option>
                <option value="event%20management">Event Management</option>
                <option value="facebook%20marketing">Facebook Marketing</option>
                <option value="fashion%20design">Fashion Design</option>
                <option value="film%20making">Film Making</option>
                <option value="finance">Finance</option>
                <option value="flutter%20development">Flutter Development</option>
                <option value="front%20end%20development">Front End Development</option>
                <option value="full%20stack%20development">Full Stack Development</option>
                <option value="fundraising">Fundraising</option>
                <option value="game%20development">Game Development</option>
                <option value="general%20management">General Management</option>
                <option value="government">Government</option>
                <option value="graphic%20design">Graphic Design</option>
                <option value="hospitality">Hospitality</option>
                <option value="hotel%20management">Hotel Management</option>
                <option value="hr">Human Resources (HR)</option>
                <option value="humanities">Humanities</option>
                <option value="image%20processing">Image Processing</option>
                <option value="industrial%20and%20production%20engineering">Industrial &amp; Production Engineering</option>
                <option value="industrial%20design">Industrial Design</option>
                <option value="information%20technology">Information Technology</option>
                <option value="instrumentation%20and%20control%20engineering">Instrumentation &amp; Control Engineering</option>
                <option value="interior%20design">Interior Design</option>
                <option value="internet%20of%20things%20(iot)">Internet of Things (IoT)</option>
                <option value="ios%20app%20development">iOS App Development</option>
                <option value="java">Java Development</option>
                <option value="javascript%20development">Javascript Development</option>
                <option value="journalism">Journalism</option>
                <option value="law">Law</option>
                <option value="legal%20research">Legal Research</option>
                <option value="machine%20learning">Machine Learning</option>
                <option value="manufacturing%20engineering">Manufacturing Engineering</option>
                <option value="market%2Fbusiness%20research">Market/Business Research</option>
                <option value="marketing%2Fsales">Marketing/Sales</option>
                <option value="material%20science">Material Science</option>
                <option value="mathematics">Mathematics</option>
                <option value="mathematics%20and%20computing">Mathematics &amp; Computing</option>
                <option value="mba">MBA</option>
                <option value="mechanical">Mechanical Engineering</option>
                <option value="mechatronics">Mechatronics</option>
                <option value="media">Media</option>
                <option value="medicine">Medicine</option>
                <option value="merchandise%20design">Merchandise Design</option>
                <option value="mobile%20app%20development">Mobile App Development</option>
                <option value="motion%20graphics">Motion Graphics</option>
                <option value="music">Music</option>
                <option value="naval%20and%20ocean">Naval Architecture and Ocean Engineeering</option>
                <option value="network%20engineering">Network Engineering</option>
                <option value="ngo">NGO</option>
                <option value="node.js%20development">Node.js Development</option>
                <option value="operations">Operations</option>
                <option value="petroleum%20engineering">Petroleum Engineering</option>
                <option value="pharmaceutical">Pharmaceutical</option>
                <option value="photography">Photography</option>
                <option value="php%20development">PHP Development</option>
                <option value="physics">Physics</option>
                <option value="political%2Feconomics%2Fpolicy%20research">Political/Economics/Policy Research</option>
                <option value="pr">Public Relations (PR)</option>
                <option value="product">Product Management</option>
                <option value="programming">Programming</option>
                <option value="project%20management%20">Project Management </option>
                <option value="proofreading">Proofreading</option>
                <option value="psychology">Psychology</option>
                <option value="python%2Fdjango">Python/Django Development</option>
                <option value="recruitment">Recruitment</option>
                <option value="ruby%20on%20rails">Ruby on Rails</option>
                <option value="science">Science</option>
                <option value="search%20engine%20optimization%20(seo)">Search Engine Optimization (SEO)</option>
                <option value="social%20media%20marketing">Social Media Marketing</option>
                <option value="social%20work">Social Work</option>
                <option value="software%20development">Software Development</option>
                <option value="software%20testing">Software Testing</option>
                <option value="statistics">Statistics</option>
                <option value="strategy">Strategy</option>
                <option value="subject%20matter%20expert%20(sme)">Subject Matter Expert (SME)</option>
                <option value="supply%20chain%20management%20(scm)">Supply Chain Management (SCM)</option>
                <option value="talent%20acquisition">Talent Acquisition</option>
                <option value="teaching">Teaching</option>
                <option value="telecalling">Telecalling</option>
                <option value="transcription">Transcription</option>
                <option value="translation">Translation</option>
                <option value="travel%20and%20tourism">Travel &amp; Tourism</option>
                <option value="ui%2Fux">UI/UX Design</option>
                <option value="video%20making%2Fediting">Video Making/Editing</option>
                <option value="videography">Videography</option>
                <option value="volunteering">Volunteering</option>
                <option value="web%20development">Web Development</option>
                <option value="wordpress%20development">Wordpress Development</option>
"""

soup0 = BeautifulSoup(category_,"lxml")

all_categories = soup0.find_all("option")
available = []
value = []

for i in all_categories:
    available.append(i.text)
    value.append(i["value"])


print("""
        Press 1, To see the some Available domains of Internships

        Press 2, To Search for your interested areas of Internship
""")
print()
d = "y"

while d=="y" or d=="Y":
    c = input("Enter Your choice (1/2): ")
    print()
    if c=="1":
        for i in available:
            print(i)
        print()
        d = input("Do You Want to Continue (y/n): ")
        print()

    elif c=="2":
        print()
        i = input("Enter Your Interested Area: ")
        print()

        if i in available:
            s = value[available.index(i)]
            print()

            html_txt = requests.get(f"https://internshala.com/internships/"+str(s)+"-internship/").text

            soup = BeautifulSoup(html_txt,"lxml")

            interships = soup.find("div", id = "internship_list_container_1")

            individual_internships = interships.find_all("div", class_ = "heading_4_5 profile")

            company_name = interships.find_all("a", class_ = "link_display_like_text")

            location = interships.find_all("div", id = "location_names")

            link = interships.find_all("div", class_ = "button_container")

            other_details = interships.find_all("div", class_ ="internship_other_details_container")

            for a,b,c,d,e in zip(individual_internships,company_name,location,link,other_details):
                print(f"Internship Topic : {a.text.strip()}")
                print()
                print("Company Name :", b.text.strip())
                print()

                x = c.span.find_all("a",class_ = "location_link")
                y = []
                for i in x:
                    y.append(i.text)

                print("Location of Internship :",y)
                print()
                print("More Information : https://internshala.com"+str(d.a["href"]))
                print()
                print("Stipend (in Rs.) :", e.find_all("div",class_="item_body")[2].text.strip())
                print()
                print("Last date to apply :", e.find_all("div",class_="item_body")[3].text.strip())
                print()
                print("Duration :", e.find_all("div",class_="item_body")[1].text.strip())
                print()
                print()
                print()
                print()
            d = input("Do You Want to Continue (y/n): ")
            print()

        else:
            print("Please choose from available Topics to get accurate results...")
            print()
            d = input("Do You Want to Continue (y/n): ")
            print()

    else:
        print("Wrong Choice")
        print()
        d = input("Do You Want to Continue (y/n): ")
        print()