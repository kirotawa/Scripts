<?php
 /* GOALS: 
 * - Numer of entries
 * - Number of errors 
 * - Number of success
 * - What files were visited more often
 * - the most popular refers and their percentagem
 * */

# Log file format: <origin> [<date_time>] "<method_and_file>" <status> <bytes> "<refer>"
$file = fopen("file.log", "r");

# exp regs
$origin = "\d+.\d+.\d+.\d+";
$date_time = "\[[^\[\]:]+:\d+:\d+:\d+ [\-\+]?\d\d\d\d\]";
$method_and_file = "\"\w+ (?P<filepath>[\S]+) [^\"]+";
$status = "(?P<status>\d+)";
$bytes = "(-|\d+)";
$refers = "(?P<refer>\"[^\"]*\")";

# hash table in order to count entries we are interesting int
$hash_table = [];
$hash_table["refers"] = [];
$hash_table["files"] = [];
$entries = 0;

while($line = fgets($file)) {
    preg_match('/'.$origin.' - - '.$date_time.' '.$method_and_file.'\" '.$status.' '.$bytes.' '.$refers.'/', $line, $matches);

    if ($matches["status"] >=200 && $matches["status"] <= 226) {
        if (!array_key_exists("success", $hash_table)) {
            $hash_table["success"] = 1;
        }
         else {
            $hash_table["success"] += 1;   
        }
    }
    if ($matches["status"] >=400 && $matches["status"] <= 599) {
        if (!array_key_exists("errors", $hash_table)) {
            $hash_table["errors"] = 1;
        }
         else {
            $hash_table["errors"] += 1;   
        }
    }
  
    if (!array_key_exists($matches["filepath"], $hash_table["files"])) {
            $hash_table["files"][$matches["filepath"]] = 1;
    }
    else {
       $hash_table["files"][$matches["filepath"]] += 1;   
    }

    if (!array_key_exists($matches["refer"], $hash_table["refers"])) {
            $hash_table["refers"][$matches["refer"]] = 1;
    }
    else {
       $hash_table["refers"][$matches["refer"]] += 1;   
    }
    $entries += 1;
}
fclose($file);

echo "Total entries: ".$entries." <br>";
echo "Errors: ".$hash_table["errors"]."<br>";
echo "Success: ".$hash_table["success"]."<br";

arsort($hash_table["refers"]);
arsort($hash_table["files"]);

echo "<br><br>";
echo "The top 3 visited files were: <br>";

$i = 0;
for ($i; $i < 3; $i++)
{
    $file = key($hash_table["files"]);
    echo $i+1;
    echo " ".$file." <br>";
    next($hash_table["files"]);
}

$key_refer = key($hash_table["refers"]);
echo "The most popular refer is: ".$key_refer."<br>";
echo "In percentage: ".number_format(($hash_table["refers"][$key_refer]*100)/$entries,2, '.', '')."%";

?>
