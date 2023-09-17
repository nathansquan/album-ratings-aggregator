# Album Ratings Aggregator

## Objective

The purpose of this project will be to create a to create a a tool that provides the user with information about music album ratings aggregated across multiple music review sources.

## High Level Requirements

1. The aggregator should allow the user to filter by different key grouping like artist, genre, date released, etc.
2. The tool should display high level metrics
3. The tool should allow the user to drill down and get more context about the metrics

## Metrics

- Average rating for an album
- Average album rating for an artist

## Data Sources

### Reviews

- [Pitchfork](https://pitchfork.com/reviews/albums/) scraping
- [AllMusic](https://www.allmusic.com/newreleases) scraping
- [theneedledrop](https://www.youtube.com/@theneedledrop) YouTube API

### Album Data

- Spotify API


## Infrastructure

## Dimensional Modeling

Use Kimball 4-step dimensional modeling process.

### Select the Business Process

The business process is the music album review.

### Declare the Grain

The grain is the album review.

### Identify Dimensions

- Review
    - Publisher
    - Author
    - Date
- Album
    - Release date
- Artist 
    - Name

### Identify the Facts

- Album rating

