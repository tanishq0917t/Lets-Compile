from flask import *
import subprocess
import os
app = Flask(__name__)
@app.route('/')
def upload():
    return render_template("upload.html")


def cleanTemp():    #Helper function to clean up dump files which are created at runtime at server end
    subprocess.run(["rm","output.txt"])
    subprocess.run(["rm","error.txt"])


@app.route('/sample')
def sample():
    return render_template("sample.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        isThereAnyInputFile=True
        try:
            fi = request.files['inputFile']
            fi.save(fi.filename)
        except:
            isThereAnyInputFile=False
        ot=""
        if(f.filename.endswith(".c")):
            with open("output.txt","w+") as outputFile:
                with open("error.txt","w+") as errorFile:
                    subprocess.run(["gcc",f.filename,"-o",f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile)
                    if os.stat("error.txt").st_size==0:
                        if isThereAnyInputFile:
                            with open(fi.filename,"r") as inputContent:
                                subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile,stdin=inputContent)
                                subprocess.run(["rm",fi.filename])      #dumping up the testcase file created at server end
                        else:
                            subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile)
                        outputFile.close()
                        with open("output.txt") as outputFile:
                            with open("ot.txt","w+") as otFile:
                                while(True):
                                    m=str(outputFile.readline())
                                    if m=="": break
                                    otFile.write(m)
                        subprocess.run(["rm",f.filename])
                        subprocess.run(["rm",f.filename[:-2]+".out"])
                        ot=open("ot.txt","r").read().replace("\n","<br>")
                        subprocess.run(["rm","ot.txt"])
                        print(ot)
                    elif os.stat("error.txt").st_size!=0 and open("error.txt").read().find("error:")==-1:
                        if isThereAnyInputFile:
                            with open(fi.filename,"r") as inputContent:
                                subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile,stdin=inputContent)
                                subprocess.run(["rm",fi.filename])      #dumping up the testcase file created at server end
                        else:
                            subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile)
                        outputFile.close()
                        with open("output.txt") as outputFile:
                            with open("ot.txt","w+") as otFile:
                                while(True):
                                    m=str(outputFile.readline())
                                    if m=="": break
                                    otFile.write(m)
                        subprocess.run(["rm",f.filename])
                        subprocess.run(["rm",f.filename[:-2]+".out"])
                        ot=open("ot.txt","r").read().replace("\n","<br>")
                        subprocess.run(["rm","ot.txt"])
                        print(ot)
                    else:
                        #Error Zone
                        errorFile.close()
                        with open("error.txt") as errorFile:
                            with open("ot.txt","w+") as otFile:
                                while(True):
                                    m=str(errorFile.readline())
                                    if m=="": break
                                    otFile.write(m)
                        ot=open("ot.txt","r").read().replace("\n","<br>")
                        subprocess.run(["rm","ot.txt"])
                        subprocess.run(["rm",f.filename])
                        cleanTemp()
                        return render_template("failure.html", output=ot)
        if(f.filename.endswith(".cpp")):
            with open("output.txt","w+") as outputFile:
                with open("error.txt","w+") as errorFile:
                    subprocess.run(["g++",f.filename,"-o",f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile)
                    if os.stat("error.txt").st_size==0:
                        if isThereAnyInputFile:
                            with open(fi.filename,"r") as inputContent:
                                subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile,stdin=inputContent)
                                subprocess.run(["rm",fi.filename])      #dumping up the testcase file created at server end
                        else:
                            subprocess.run(["./"+f.filename[:-2]+".out"],stdout=outputFile,stderr=errorFile)
                        outputFile.close()
                        with open("output.txt") as outputFile:
                            with open("ot.txt","w+") as otFile:
                                while(True):
                                    m=str(outputFile.readline())
                                    if m=="": break
                                    otFile.write(m)
                        subprocess.run(["rm",f.filename])
                        subprocess.run(["rm",f.filename[:-2]+".out"])
                        ot=open("ot.txt","r").read().replace("\n","<br>")
                        subprocess.run(["rm","ot.txt"])
                        print(ot)
                    else:
                        #Error Zone
                        errorFile.close()
                        with open("error.txt") as errorFile:
                            with open("ot.txt","w+") as otFile:
                                while(True):
                                    m=str(errorFile.readline())
                                    if m=="": break
                                    otFile.write(m)
                        ot=open("ot.txt","r").read().replace("\n","<br>")
                        subprocess.run(["rm","ot.txt"])
                        subprocess.run(["rm",f.filename])
                        cleanTemp()
                        return render_template("failure.html", output=ot)
        if(f.filename.endswith(".py")):
            with open("output.txt","w+") as outputFile:
                with open("error.txt","w+") as errorFile:
                    if isThereAnyInputFile:
                        with open(fi.filename,"r") as inputContent:
                            subprocess.run(["python3",f.filename],stdout=outputFile,stderr=errorFile,stdin=inputContent)
                            subprocess.run(["rm",fi.filename])      #dumping up the testcase file created at server end
                    else:
                        subprocess.run(["python3",f.filename],stdout=outputFile,stderr=errorFile)
            if os.stat("error.txt").st_size==0:
                ot=open("output.txt").read().replace("\n","<br>")
                cleanTemp()
                return render_template("success.html",output=ot)
            else:
                print("In python Error zone")
                ot=open("error.txt").read().replace("\n","<br>")
                cleanTemp()
                return render_template("failure.html",output=ot)
        cleanTemp()
        return render_template("success.html", output=ot)
if __name__ == '__main__':
    app.run(debug = True)
