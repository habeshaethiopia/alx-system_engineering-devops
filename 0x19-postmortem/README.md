<!-- postmortem -->
<!DOCTYPE html>
<html>
<head>

</head>
<body>

  <div class="section">
  <h2 class="summary">Summary:</h2>
  On NOV 8 2023, an incident occurred in my server due to a misspelling in the Apache config file. The file was mistakenly configured to use the file extension ".phpp" instead of the correct ".php" extension. This resulted in unexpected behavior and caused disruptions to the web server's functionality.
</div>
</div>

<!-- Insert your interactive image with a link here -->
<div class="image-container">
  <a href="">
    <img class="clickable-image" src="https://www.figma.com/community/thumbnail?resource_id=754026612866636376&resource_type=plugin" alt="Inspiring Image" />
  </a>
</div>

<div class="section">
  <h2 class="timeline">Timeline:</h2>
  <ol>
    <li>[6:00]: The Apache config file was modified by an administrator to update certain settings.</li>
    <li>[6:25]: The administrator inadvertently misspelled the file extension as ".phpp" instead of ".php".</li>
    <li>[6:29]: The web server was restarted to apply the changes made in the config file.</li>
    <li>[6:30]: Users started reporting errors when accessing PHP-based web pages.</li>
    <li>[7:00]: The IT team was alerted about the issue and began investigating the cause.</li>
    <li>[11:00]: The misconfiguration in the Apache config file was identified as the root cause of the problem.</li>
    <li>[12:00]: The misconfiguration was rectified by correcting the file extension to ".php".</li>
    <li>[1:00] PM: The web server was restarted to apply the corrected configuration.</li>
    <li>[1:30] PM: Verification tests were performed to ensure that the issue was resolved.</li>
    <li>[1:31] PM: Users confirmed that they were able to access PHP-based web pages without any errors.</li>
  </ol>
</div>

<div class="section">
  <h2 class="root-cause">Root Cause:</h2>
  The root cause of this incident was determined to be human error. The administrator responsible for modifying the Apache config file mistakenly entered ".phpp" as the file extension instead of ".php". This simple typographical error went unnoticed during the configuration process, leading to the subsequent disruptions.
</div>

<div class="section">
  <h2 class="resolution">Resolution and Preventive Measures:</h2>
  To resolve the issue, the misconfiguration in the Apache config file was corrected by changing the file extension from ".phpp" to ".php". The web server was then restarted to apply the corrected configuration. Verification tests were conducted to ensure that the problem was resolved, and users confirmed that they could access PHP-based web pages without encountering any errors.
  
  To prevent similar incidents from occurring in the future, the following preventive measures will be implemented:
  <ol>
    <li>Double-checking: Administrators will be reminded to double-check their changes before applying them to critical systems.</li>
    <li>Review and Approval: Any modifications to configuration files will require review and approval from a second administrator to minimize the risk of human error.</li>
    <li>Testing: Before restarting services, thorough testing procedures will be followed to identify any potential issues resulting from configuration changes.</li>
    <li>Documentation: Clear documentation outlining correct configuration settings and procedures will be maintained and made easily accessible to administrators.</li>
  </ol>
</div>

<div class="section">
  <h2 class="lessons">Lessons Learned:</h2>
  This incident highlights the importance of attention to detail when making changes to critical systems. A simple typographical error can have significant consequences, causing disruptions and impacting user experience. It is crucial for administrators to exercise caution, follow proper change management procedures, and verify their changes before implementing them in production environments. Regular reviews, testing, and documentation are essential for maintaining system stability and preventing similar incidents in the future.
</div>

</body>
</html>
