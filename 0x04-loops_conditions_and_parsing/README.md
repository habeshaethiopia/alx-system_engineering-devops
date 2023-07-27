<h1 class="gap">0x04. Loops, conditions and parsing</h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:6,&quot;value&quot;:&quot;DevOps&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:10,&quot;value&quot;:&quot;Shell&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:11,&quot;value&quot;:&quot;Bash&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:28,&quot;value&quot;:&quot;Scripting&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"><div class="align-items-center d-flex flex-wrap gap-3 my-2" 
style ="-webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    font-size: 14px;
    line-height: 1.428571429;
    color: #333333;
    box-sizing: border-box;
    align-items: center !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 1rem !important;
    margin-bottom: 10px !important;
    margin-top: 10px !important;">
<span class="label label-primary" style="font-size: 14px;">DevOps </span>
<span class="label label-primary" style="font-size: 14px;">Shell </span>
<span class="label label-primary" style="font-size: 14px;">Bash </span>
<span class="label label-primary" style="font-size: 14px;">Scripting</span>
</div></div>
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    --col-bg-400: #121212;
    --col-bg-500: #1e1f22;
    --col-bg-600: #2b2d31;
    --col-bg-700: #313338;
    --col-bg-800: #383a40;
    --col-current-date: #888672;
    --col-second-deadline: #ff00002b;
    --col-second-deadline-link: #c8bfbf;
    --col-acc-400: #df3e3e;
    --col-acc-500: #f36262;
    --col-code-color: #e55039;
    --col-quiz-pass: #38b000;
    --col-code-pass: #284724;
    --col-code-fail: #521b1b;
    --col-requirement-pass: #28472466;
    --col-requirement-fail: #521b1b66;
    --col-efficiency-success: #291531;
    --col-efficiency-fail: #7d6e18;
    --col-answer-success: #151a48;
    --col-answer-fail: #774e1d;
    --col-light-400: #fff;
    --col-light-500: #ddd3d3;
    --col-light-600: #a79a9a;
    --col-light-700: #837a7a;
    --col-light-800: #746d6d;
    --col-bg-clear: transparent;
    --darkreader-neutral-background: #212222;
    --darkreader-neutral-text: #eae3d9;
    --darkreader-selection-background: #165aaa;
    --darkreader-selection-text: #fbf5ec;
    font-family: "aktiv-grotesk", sans-serif;
    font-size: 14px;
    line-height: 1.428571429;
    color: #333333;
    box-sizing: border-box;
    align-items: center !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 1rem !important;
    margin-bottom: 10px !important;
    margin-top: 10px !important;
<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/BC2neyc5GcI" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230727%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230727T100300Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=98180cf3839abfb22b6e1d8854f9398d9a53e14d5dfc813d8daeaf983ca13420" alt="" loading="lazy" style=""></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/wT98UJfv_E2tk4yP9PcLLw" title="The <code>for</code> loop&quot; target=“_blank”>The <code>for</code> loop</a> </li>
<li><a href=" rltoken="" fsas6duzuuian6nawyxztw"="" nl_7unvltjrrh1c62_if_g"="" u93es1eshyob0odmydsvag"="" target="_blank">Loops sample</a> </li>
<li><a href="/rltoken/olvOKX699pq50rkHRE5cSA" title="Variable assignment and arithmetic" target="_blank">Variable assignment and arithmetic</a> </li>
<li><a href="/rltoken/HxohzllkOWh0t4dy_HptIQ" title="Comparison operators" target="_blank">Comparison operators</a> </li>
<li><a href="/rltoken/g8of2ABPEJfCNtPrDQaqVw" title="File test operators" target="_blank">File test operators</a> </li>
<li><a href="/rltoken/O0Ay21p7tDhfLMsYbtAKug" title="Make your scripts portable" target="_blank">Make your scripts portable</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>env</code></li>
<li><code>cut</code></li>
<li><code>for</code></li>
<li><code>while</code></li>
<li><code>until</code></li>
<li><code>if</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/UnkzDNdH09TFJ0-Y56azyg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.7.0</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>More Info</h2>

<h3>Shellcheck</h3>

<p><a href="/rltoken/joK6l_yEZ9N7T0GQ1RDjLA" title="Shellcheck" target="_blank">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. <code>Shellcheck</code> is your friend! <strong>All your Bash scripts must pass <code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>

<p><code>Shellcheck</code> is available on the school’s computers. If you want to use it on your own computer, here is how to <a href="/rltoken/jbz0_-i3TV3WpKgxhyrtpA" title="install it" target="_blank">install it</a>.</p>

<p>Examples:</p>

<p>Not passing <code>Shellcheck</code>:<br>
<br>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png" alt="" loading="lazy" style=""></p>

<p>Passing <code>Shellcheck</code>:<br>
<br>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png" alt="" loading="lazy" style=""></p>

<p>For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code <code>SC2034</code>, you can browse <a href="/rltoken/dxp49_rfO4_9Yjtcg59exg" title="https://github.com/koalaman/shellcheck/wiki/SC2034" target="_blank">https://github.com/koalaman/shellcheck/wiki/SC2034</a>.</p>

  </div>
</div>
