[![ci](https://github.com/paperless-ngx/paperless-ngx/workflows/ci/badge.svg)](https://github.com/paperless-ngx/paperless-ngx/actions)
[![Crowdin](https://badges.crowdin.net/paperless-ngx/localized.svg)](https://crowdin.com/project/paperless-ngx)
[![Documentation Status](https://img.shields.io/github/deployments/paperless-ngx/paperless-ngx/github-pages?label=docs)](https://docs.paperless-ngx.com)
[![codecov](https://codecov.io/gh/paperless-ngx/paperless-ngx/branch/main/graph/badge.svg?token=VK6OUPJ3TY)](https://codecov.io/gh/paperless-ngx/paperless-ngx)
[![Chat on Matrix](https://matrix.to/img/matrix-badge.svg)](https://matrix.to/#/%23paperlessngx%3Amatrix.org)
[![demo](https://cronitor.io/badges/ve7ItY/production/W5E_B9jkelG9ZbDiNHUPQEVH3MY.svg)](https://demo.paperless-ngx.com)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/paperless-ngx/paperless-ngx/blob/main/resources/logo/web/png/White%20logo%20-%20no%20background.png" width="50%">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/paperless-ngx/paperless-ngx/raw/main/resources/logo/web/png/Black%20logo%20-%20no%20background.png" width="50%">
    <img src="https://github.com/paperless-ngx/paperless-ngx/raw/main/resources/logo/web/png/Black%20logo%20-%20no%20background.png" width="50%">
  </picture>
</p>

<!-- omit in toc -->

# Natural Stupidity  

**Natural Stupidity** is a next-generation document management system that leverages AI and cloud technology to streamline document organization, search, and collaboration.  

## Key Features  
- **Automated Classification & Tagging**  
  - AI-powered categorization of documents (invoices, contracts, resumes)  
  - Smart tagging using text analysis for better organization  

- **Intelligent Content Extraction & Metadata Generation**  
  - OCR-based extraction of key details such as dates, amounts, and names  
  - Enhances searchability and document organization  

- **Next-Gen Document Handling**  
  - Smart search with advanced filters  
  - Version control to track document changes  
  - Collaborative editing for real-time teamwork  

- **Cloud-Powered Solution**  
  - Built on **Azure** for scalability, security, and efficient cloud storage  

## Live Demo  
Try out **Natural Stupidity** with a live demo:  
[demo.natural-stupidity.com](https://demo.natural-stupidity.com)  
> Use **demo / demo** as login credentials. (Note: Demo content resets frequently, do not upload sensitive information.)  

## Installation  
The easiest way to deploy **Natural Stupidity** is **Docker Compose**. The files in the `/docker/compose` directory are configured to pull the image from the **GitHub Container Registry**.  

If you'd like to jump right in, you can configure a **Docker Compose** environment with our install script:  

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
