aws17={
        'general': {
        "shapes": [ 'management console', 'cloud','forums', 'virtual private cloud'],
        "strokeColor": "#D86613",
        "fillColor": "#D86613"
        },
    'compoute':{
        "shapes": [ 'ami', 'ec2'],
        "strokeColor": "#D86613",
        "fillColor": "#D86613"
    },
    'iot':{
        "shapes": [ 'iot', 'greengrass', 'action', 'actuator'],
        "strokeColor": "#5294CF",
        "fillColor": "#5294CF"

    },
    'analytics':{
        "shapes": [ 'athena', 'cloudsearch', 'elasticsearchservice', 'kinesis'],
        "strokeColor": "#5294CF",
        "fillColor": "#5294CF"

    }
}

fh2 =open("code.js", 'w')

for groupname in aws17.keys():
    print("-"*30)
    print("GROUPNAME", groupname)
    print("-"*30)
    found = False
    fh = open(groupname.lower() + ".xml", 'w')
    fh.write("<shapes name=\"mxgraph." + groupname + "\">\n")
    for component in aws17[groupname]['shapes']:
        xmlcontent = []
        found = False
        for line in open("data.xml"):
            if '"'+component.lower() +'"' in line.lower() and not found:
                print("FOUND:\t\t", component)
                found = True
                xmlcontent.append(line)
            elif found:
                xmlcontent.append(line)
                if('</shape>' in line):
                    found = False
        if xmlcontent:
            fh.writelines(xmlcontent)
        else:
            print("NOT FOUND:\t", component)
    fh.write("</shapes"+">")
    fh.close()
    fh2.write("this.addStencilPalette('AWS', 'AWS " + groupname.title() +"', dir + '/aws17/"+groupname.lower()+".xml',';whiteSpace=wrap;html=1;fillColor="+aws17[groupname]['fillColor']+";strokeColor="+aws17[groupname]['strokeColor']+";strokeWidth=1');\n")

fh2.close()

