# Backscatter Metadata

## Background

So you have just created a backscatter mosaic with your multibeam data processing software and exported it as a .tif file. Now how do you inform this file's future users about all that this file represents?

Typically, you would write some information in the file's name: most likely the word "backscatter" or the initials "BS" at the very least, but also perhaps the survey area or surveyor name, and the survey year. For more information, maybe you can add the sonar model, or the grid size, or the version of that mosaic. So something like:

   `Clinton-2022-m-block34_BS_v3.tif`

Congratulations! You have started creating metadata.

The problem is that there is a limit to filenames length, so what about all the rest of the information? What about the frequency? The software used? The processing applied? The files that went in? Or even your name as the author?

A proper data management practice would be to compile all the relevant information together to live alongside the mosaic file. For even better practice, you would follow a template (so that all mosaic files have a metadata in the same format), and write this information in a manner that is readable both by humans and machines.

This repository proposes such a metadata template and style.

## Core Principles

* Human-friendliness:
    * Enough information to provide a good overview, but not so much that it is overwhelming and difficult to parse.
    * Descriptive and unambiguous field names
    * Broken down in thematic sections
    * Every field to be optional (just fill what you can)
    * No requirements on fields format (number, text, boolean, etc.)

* Machine-friendliness:
    * Machine-readable formats
    * Version control

## Basic Template Contents

The proposed template is to collate the basic information as pairs of field-value, organized into six thematic sections, or "parent nodes". 

We list below our proposed sections and field-value pairs. See further below for the implementation.

### 1. survey
A section containing the basic information about the survey that produced the dataset from which the mosaic was created:

|Parent node|Field|Description|Example|
|---|---|---|---|
|survey|project|Name of project|MAREANO
|survey|year|Year of survey|2022
|survey|client|Name of client|Kartverket
|survey|surveyor|Name of surveyors|Clinton Marine Survey
|survey|site|Name of site|B34
|survey|vessel|Name of vessel|Northern Storm
|survey|sonarModel|Name of sonar model|Kongsberg EM2040
|survey|sonarSerialNumber|Serial number of sonar system|2106
|survey|comments|Free text field|Surveyed over Aug 21-23, 2022 

No need to go into too many details here since this information is most likely also present in reports, and bathymetry metadata. In fact, the information in this section can most likely be directly obtained from any existing "acquisition metadata".

### 2. data
A section containing the basic information about the data that went into the mosaic:

|Parent node|Field|Description|Example|
|---|---|---|---|
|data|frequencyKHz|Operating frequency in kHz|300
|data|pulseLengthMicroSec|Pulse length in microseconds|0.000107
|data|acquisitionMode|Sonar acquisition mode|Medium CW
|data|filesList|List of raw data files used in mosaic separated by semicolons|All files available 
|data|comments|Free text field|Very wide range of absorption coefficients in data

The difference with the previous section is that the information here might be variable within the dataset, so while the information from the previous section could be just copied-and-pasted from the "acquisition metadata", this one may here need some adjustment by the author of the mosaic. For example, we include here the list of files that actually went into the mosaic, or the frequency used for the mosaic (the dataset may be multispectral). 

Writing settings here (frequency, acquisition mode) also emphasize the typical recommendation that backscatter mosaics be produced using data acquired in a constant setting.

### 3. processing
A section containing the basic information about the processing applied to the data to produce the mosaic:

|Parent node|Field|Description|Example|
|---|---|---|---|
|processing|softwareName|Name of processing software|QPS FMGT
|processing|softwareVersion|Version of processing software|7.10.3
|processing|comments|Free text field|None

Very basic here because any further details would be software-dependent. See below on how to augment this section with processing details.

### 4. mosaic
A section containing the basic information about the mosaic created:

|Parent node|Field|Description|Example|
|---|---|---|---|
|mosaic|author|Mosaic author|Alexandre Schimel
|mosaic|date|Date of mosaic creation|09/03/2023
|mosaic|filename|Mosaic file name|Clinton-2022-m-block34_BS_v3.tif
|mosaic|projection|Mosaic datum and projection|WGS84-UTM31N
|mosaic|pixelSizeM|Pixel size in meters|1
|mosaic|status|Mosaic version|v3 (preliminary)
|mosaic|comments|Free text field|Still a few artefacts to correct

### 5. qualityControl
A section containing the basic information about any quality control performed on the mosaic itself:

|Parent node|Field|Description|Example|
|---|---|---|---|
|qualityControl|author|QC author|Margaret Dolan
|qualityControl|date|QC date|09/03/2023
|qualityControl|grade|Quality grade|good
|qualityControl|comments|Free text field|None

### 6. metadata
A section containing information about this metadata template:

IMPORTANT: Do not change the VALUES of those fields as they allow identifying this specific template.

|Parent node|Field|Description|VALUES|
|---|---|---|---|
|metadata|name|Authority for this metadata template (DO NOT CHANGE)|NGU
|metadata|version|Version of this metadata template (DO NOT CHANGE)|0.4
|metadata|author|Authors of this metadata template (DO NOT CHANGE)|NGU (Alexandre Schimel; Margaret Dolan)
|metadata|date|Date of creation of this metadata template (DO NOT CHANGE)|08/09/2023

If you wish to modify this template, either mention it in the "comments" field, or contact us to produce a new version.

|Parent node|Field|Description|Example|
|---|---|---|---|
|metadata|comments|Free text field|Template modified from original by John Smith, Antarctic Hydrographic Survey, on 03/072036

## Augmenting the Processing Section

Additional information about the processing applied would be welcome. Here is for example a set of fields that are applicable to software FMGT v7.10.3.

|Parent node|Field|Description|Example|
|---|---|---|---|
|processing|sourceData|Source Data|Beam time series
|processing|referenceGridFilename|Reference grid filename|B34_GRIDNODES.tif
|processing|absorptionCoefficient|Absorption coefficient|0 (default)
|processing|backscatterRangeMin|Backscatter range minimum value|-70 (default)
|processing|backscatterRangeMax|Backscatter range maximum value|10 (default)
|processing|AVG_algorithm|AVG algorithm name|Flat
|processing|AVG_windowSize|AVG window size in pings|300
|processing|AVG_referenceBand|AVG reference band|Adaptive
|processing|AVG_applyAcrossLineBreaks|AVG Apply Across Line Breaks|FALSE
|processing|navigationTimeWindow|Navigation time window|5
|processing|useAllSoundings|Use all soundings checkbox|TRUE
|processing|lineBlending|Line blending|20
|processing|mosaicStyle|Mosaic style|blend
|processing|filteringType|Filtering type|dB Mean
|processing|fillGaps|Fill gaps|TRUE

The problem here is that these fields are dependent on the processing software and the methodology used. If we use a different software, or a different version of the software, or even simpler we use a new method from the same software and version, this entire set needs to be modified. And if we do this, then the entire template is modified with every minute change in processing, and it is no longer a template.

The way to solve this is that to control these processing details as a sub-template, with its own version control. 

Below is the additional field for version-control:

|Parent node|Field|Description|Example|
|---|---|---|---|
|processing|processingMetadataSchema|Version number for this processing sub-template (DO NOT CHANGE)|FMGT_v7.10.3_RevB


## In practice

The proposed template can be put in practice in any way you see fit. 

You can:
* Save this information in a file that sits next to the mosaic, add it to an ArcGIS metadata file, in a database, or embedded in the geotiff's metadata.
* If saved as a text file, you can format this information as XML, json, (or other machine-readable formats), .csv, plain text, excel file (or other human-readable formats).

Our recommendation is to save all this information into a text file following the JSON format (see example below) so that it is both Machine- and Human-readable and to give this file the same (or similar) name as the mosaic tif file so they can be kept together at all times. 

Contents of text file `Clinton-2022-m-block34_BS_v3.json`:
```
{
    "metadata": {
        "name": "NGU",
        "version": "0.4",
        "author": "NGU (Alexandre Schimel; Margaret Dolan)",
        "date": "08/09/2023"
    },
    "survey": {
        "project": "MAREANO",
        "year": 2022,
        "client": "Kartverket",
        "surveyor": "Clinton Marine Survey",
        "site": "B34",
        "vessel": "Northern Storm",
        "sonarModel": "Kongsberg EM2040",
        "sonarSerialNumber": 2106,
        "comments": "Surveyed over Aug 21-23, 2022"
    },
    "data": {
        "frequencyKHz": 300,
        "pulseLengthMicroSec": 0.000107,
        "acquisitionMode": "Medium CW",
        "filesList": "All files available",
        "comments": "Very wide range of absorption coefficients in data"
    },
    "processing": {
        "processingMetadataSchema": "FMGT_v7.10.3_RevB",
        "softwareName": "QPS FMGT",
        "softwareVersion": "7.10.3",
        "sourceData": "Beam time series",
        "referenceGridFilename": "B34_GRIDNODES.tif",	
        "absorptionCoefficient": "0 (default)",
        "backscatterRangeMin": "-70 (default)",
        "backscatterRangeMax": "10 (default)",
        "AVG_algorithm": "Flat",
        "AVG_windowSize": 300,
        "AVG_referenceBand": "Adaptive",
        "AVG_applyAcrossLineBreaks": false,
        "navigationTimeWindow": 5,
        "useAllSoundings": true,
        "lineBlending": 20,
        "mosaicStyle": "blend",
        "filteringType": "dB Mean",
        "fillGaps": true,
        "comments": "None"
    },
    "mosaic": {
        "author": "Alexandre Schimel",
        "date": "09/03/2023",
        "filename": "Clinton-2022-m-block34_BS_v3.tif",
        "projection": "WGS84-UTM31N",
        "pixelSize": 1,
        "status": "v3 (preliminary)",
        "comments": "Still a few artefacts to correct"
    },
    "qualityControl": {
        "author":"Margaret Dolan",
        "date": "09/03/2023",
        "grade": "good",
        "comments": "None"
    }
}
```

## Authors

* Alexandre Schimel ([The Geological Survey of Norway](https://www.ngu.no), alexandre.schimel@ngu.no)
* Margaret Dolan (The Geological Survey of Norway)
