<#
        .SYNOPSIS
        Badanie czy plik jest bezpieczny

        .DESCRIPTION
        Skrypt wysyla zapytanie do API VirusTotal z hashem podanego pliku aby sprawdzic czy jest bezpieczny a nastepnie interpretuje wynik.

        .PARAMETER FileName
        Określa nazwe pliku z rozszerzeniem np. plik.txt .


        .EXAMPLE
        PS> .\7.1.ps1 -FileName

#>
param(
        [Parameter(Mandatory = $true)]
        [string]$FileName

)

#Wygenerowanie hasha z podanego pliku 
$hash = Get-FileHash $FileName

#Wczytanie danych do headera zapytania i wysłanie zapytania do api VirusTotal
$headers=@{}
$headers.Add("accept", "application/json")
$headers.Add("x-apikey", "e4ccb1eb241622f1828b2c4d778850d54db6024f93904d500060808ef26a6458")
$response = Invoke-WebRequest -Uri "https://www.virustotal.com/api/v3/files/$($hash.Hash)" -Method GET -Headers $headers

#Przekonwertowanie danych z odpowiedzi na format Json
$responseJson = $response.Content | ConvertFrom-Json

#Liczba oznaczeń pliku jako złośliwy
$response_malicious = $responseJson.data.attributes.last_analysis_stats.malicious

#Jeśli któryś z VirusTotal oznaczył plik jako złośliwy to wtedy uznajemy go za niebezpieczny, a inaczej to jest bezpieczny
if ($response_malicious -gt 0){
    Write-Host "Plik moze byc niebezpieczny"
}
else{
    Write-Host "Plik jest bezpieczny"
}