# The Broken User (200 points)

> Not all stories have a happy ending. Like the story of Bob who deleted one of our important backups by gaining access to an S3 bucket. We have setup an environment that attempts to mimic the steps the Bob may have possibly taken to hurt our finances while having access to partial credentials of one of our other users. See if you can get the flag by using the environment. You may start here http://rogueuser.cloudvillagectf.co/index.html

**Partial AWS credentials listed on the website**

Partial AWS access key: `VTXFIGNDUZ3E`

AWS secret key: `psLn2FftAVZBPZQABNLbyHXMKK4b0bWkzsSk498+`

## Background

During the CTF, my team was unable to solve this. In particular, the codes that I wrote was simply too slow. After the CTF, I took a peek at the 2nd team's [writeup](https://tvd.dev/defcon28-cloud-village-ctf-writeup.html) for inspiration! 90 minutes was an impressive record considering CTF conditions. It was truly inspirational, considering that she was the only member in the team and yet still beat the rest of us!

Looking at her codes, I wonder if I can optimise the results further! Thus, this repository is a result of the experiment. I managed to use 5 x T2 Medium instanc(s) to do the brute force under around 36 minutes. It was really about who can do it faster. But I was trying to understand the intricacies of brute-forcing of AWS credentials. I want to identify the conditions and optimise the environment to do such attacks at a lower cost.

## Setup

In your EC2 instance, perform the following setup.

1. Install dependencies

``` bash
sudo yum check-update
sudo yum install python3 -y

sudo pip3 install requests
sudo pip3 install boto3
```

2. Use main.py to generate to generate the entries

``` bash
# use split command to slice up the files
split -n XX -d file-name
```

3. Create the AMI based off the configured instance

4. Launch X number of instances

5. SSH into each instance and launch the script

``` bash
# sample execution command
time python3 main.py call-back-url input-file
```

__The steps are highly hackish and need to be automated!__