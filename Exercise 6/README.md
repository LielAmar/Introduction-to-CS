<div align="center">
  <h1 align="center" style="border-bottom: none"><b>Exercise 6</b> - Moogle</h1>

  <p align="center">
    <b>Moogle</b> is the 6th exercise I've solved in Huji's <b>Introduction to Computer Science</b> course.
    <br>
    The main idea behind this exercise is to get familiar with <b>HTTP Requests</b>, <b>Web Scraping</b> and <b>Page Ranking</b>.
    <br>
    <br>
    <a href="https://github.com/LielAmar/Introduction-To-CS-solutions"><strong>« Home Page</strong></a>
    <br>
  </p>
</div>

<br>

<div align="left">
  <h2 align="left" style="border-bottom: 1px solid gray">Usage</h2>

  <oul align="left">
    <li>You can run the project on your personal machine by cloning this repository using <code>git clone &lt;url&gt;</code></li>
    <li>Open the cloned project in your IDE</li>
    <li><i>(Optional)</i> Create a virtual environment using <code>python3 -m venv venv</code></li>
    <li>Use <code>pip install -r requirements.txt</code> to install all required libraries</li>
    <li>run <code>python3 &lt;python file&gt;</code> to run the project</li>
  </ol>
</div>

<br>

<div align="left">
  <h2 align="left" style="border-bottom: 1px solid gray">Media</h2>

  <div align="left">
    <p>Result of executing:</p>
    <ol>
      <li><code>py moogle.py crawl https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/ indexes.txt crawl_result.pickle</code></li>
      <li><code>py moogle.py page_rank 100 crawl_result.pickle page_rank_result.pickle</code></li>
      <li><code>py moogle.py words_dict https://www.cs.huji.ac.il/w~intro2cs1/ex6/wiki/ crawl_result.pickle words_dict_result.pickleesult.pickle</code></li>
      <li><code>py moogle.py search Harry page_rank_result.pickle words_dict_result.pickle 5</code></li>
    </ol>
    <img src="./media/1.png" alt="1" width="500px" />  
  </div>
</div>

<br>

<div align="left">
  <h2 align="left" style="border-bottom: 1px solid gray">Contributing</h2>

  <p align="left">
    Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
  </p>
</div>

<br>

<div align="left">
  <h2 align="left" style="border-bottom: 1px solid gray">License</h2>

  <p align="left">
    <a href="https://choosealicense.com/licenses/mit/">Licensed under MIT</a>
  </p>
</div>