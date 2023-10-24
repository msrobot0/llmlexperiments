I could use a day off to reflect on my practice with LLM, but it is just not happening right now so persevere and sort of phone it in. In phoning it in I am generating some interesting experiments.

![](https://miro.medium.com/v2/resize:fit:1400/1*30dRevqYlrKd1pMY0qNdCQ.png)

# Today I asked:

> create a gitlab-ci pipeline that does something creative with code

I am obsessed with pipelines. It is a way to divide up code based on stage, development, testing, and deployment, and to apply certain guide rails and checks to each stage. I have a whole pipeline metaphysics that I will at some point discuss. The technological society — which is our current condition operates under pipeline metaphysics.

# The Result

> Creating a creative GitLab CI/CD pipeline largely depends on your specific project and goals, but I can provide an example of a creative pipeline that performs code analysis, generates ASCII art from your code, and then deploys it to a static website. This is a fun and unique way to visualize your code.
> 
> 1. First, make sure your repository has the following structure:
> 
> ```  
> project-root/  
> ├── .gitlab-ci.yml  
> ├── src/  
> │ ├── your_code.py  
> ├── scripts/  
> │ ├── generate_ascii_art.sh  
> ├── public/  
> ```
> 
> 2. Create a `.gitlab-ci.yml` file in the project’s root directory:
> 
> ```yaml  
> stages:  
> — build  
> — deploy
> 
> variables:  
> ARTIFACTS_DIR: artifacts  
> PUBLIC_DIR: public
> 
> generate_ascii_art:  
> stage: build  
> script:  
> — mkdir -p $ARTIFACTS_DIR  
> — ./scripts/generate_ascii_art.sh src/your_code.py > $ARTIFACTS_DIR/ascii_art.txt  
> artifacts:  
> paths:  
> — $ARTIFACTS_DIR/ascii_art.txt
> 
> deploy_to_website:  
> stage: deploy  
> only:  
> — master  
> script:  
> — cp $ARTIFACTS_DIR/ascii_art.txt $PUBLIC_DIR/index.html  
> artifacts:  
> paths:  
> — $PUBLIC_DIR  
> ```
> 
> This pipeline has two stages: `build` and `deploy`.
> 
> 3. Create the `generate_ascii_art.sh` script in the `scripts/` directory:
> 
> ```bash  
> #!/bin/bash
> 
> code_file=$1
> 
> python3 -c “  
> from art import *  
> art = text2art(open(‘$code_file’).read(), ‘block’)  
> print(art)  
> “ > ascii_art.txt  
> ```
> 
> This script uses the `art` library in Python to generate ASCII art from your code and saves it in `ascii_art.txt`.
> 
> 4. Make sure you have the `art` library installed in your Python environment. You can install it with:
> 
> ```bash  
> pip install art  
> ```
> 
> 5. Create a simple HTML template in `public/index.html` to display the generated ASCII art:
> 
> ```html  
> <!DOCTYPE html>  
> <html>  
> <head>  
> <title>Generated ASCII Art</title>  
> </head>  
> <body>  
> <pre>  
> <! — Include ASCII art here →  
> $(cat ascii_art.txt)  
> </pre>  
> </body>  
> </html>  
> ```
> 
> Now, when you push code changes to the `master` branch, GitLab CI/CD will automatically generate ASCII art from your code and deploy it to a static website. You can access the generated ASCII art by opening the website hosted in the `public` directory of your repository.
> 
> This is just one example of a creative GitLab CI/CD pipeline. You can adapt and expand upon it based on your project’s needs and the creative ideas you want to implement.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. [https://chat.openai.com](https://chat.openai.com/)

# The Commentary

This did not work out of the box — as is the case with most LLM work. But it 95% worked. And I fixed it mostly by asking follow up questions not editing the code myself. What is most impressive is that the LLM created a series of pieces, the pipeline code, the directory structure, and code run by the pipeline.

The ascii art does not generate. I suspect it has something to do with my python program that generates a Fibonacci sequence.But I am not going to debug that. Instead I am really amazed what did happen and then maybe in the future I’ll go back and revisit these early experiments.

[This project and pipeline exist in gitlab.](https://gitlab.com/m202/experiment12)

![](https://miro.medium.com/v2/resize:fit:1400/1*BarYYe-GzkHZX0QW7v-IBg.png)