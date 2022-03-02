<div align="center" style="margin: 0 auto; width: 50%;">
    <img src="images/sacred-bodies-banner.png" alt="Sacred Bodies Collection" />
    <p style="background: #800085; margin: 15px 0px; color:#000; padding: 10px; border: 3px solid #000; border-radius: 15px;">A collection of NFT items generated from Sacred Geometry, Hubble Space Telescope images, and Chakra colors.</p>
</div>

* [Official Site](https://sk33z3r.site/sacred-bodies)
* [Hubble photos use policies](https://hubblesite.org/copyright)
* [GitHub Repository](https://github.com/sk33z3r/sacred-bodies)

# IPFS Hashes

| Type       | Hash                                             |
|------------|--------------------------------------------------|
| PNG Images | `QmXHpoB7scTiutQ3Hc2Qm3EuWsMMzSGV1oqmJrX31gZoye` |
| Metadata   | `QmVpLSoYak1N8pasuxLrNZLbnvrNvLTJmY8ncMBjNRPBtQ` |

# Generation Logic

Each item is compiled by randomly choosing an attribute for each trait, each having their own chance to occur.

## Traits

### Chakra

Determines the color of the shape, and prints the associated Sanskrit Chakra name onto the image.

| Sanskrit Name | Color  | Chance (%) | No. in Collection |
|---------------|--------|------------|-------------------|
| Muladhara     | Red    | 20         | 171               |
| Svadhishtana  | Orange | 20         | 186               |
| Manipura      | Yellow | 15         | 153               |
| Anahata       | Green  | 15         | 147               |
| Vishuddha     | Blue   | 15         | 164               |
| Ajna          | Indigo | 10         | 117               |
| Sahasrara     | Purple | 5          | 62                |

### Cover Type

Determines whether the shape's color fills the image or not.

| Type | Description                                                  | Chance (%) | No. in Collection |
|------|--------------------------------------------------------------|------------|-------------------|
| Full | Color fills the image, with the shape cut out of the middle. | 85         | 810               |
| Thin | Only the shape is colored.                                   | 15         | 190               |

### Shape

Determines the shape to use.

| Shape           | Chance (%) | No. in Collection |
|-----------------|------------|-------------------|
| Flower of Life  | 10         | 117               |
| Fruit of Life   | 20         | 203               |
| Merkaba         | 35         | 293               |
| Metatron's Cube | 15         | 170               |
| Seed of Life    | 15         | 161               |
| Vesica Pisces   | 5          | 56                |

### Opacity Level

Determines the opacity level of the color layer when the type is `Full`.

| Level (%) | Chance (%) | No. in Collection |
|-----------|------------|-------------------|
| 50        | 75         | 711               |
| 35        | 25         | 289               |

### Hubble Image

Determines which Hubble Telescope image to use from a pool of 30 images.

| Image Title                      | Chance (%) | No. in Collection |
|----------------------------------|------------|-------------------|
| Abell S1063                      | 2          | 23                |
| AG Carinae                       | 2          | 32                |
| AM 2026-424                      | 2          | 14                |
| Bat Shadow                       | 4          | 38                |
| Cosmic Reef                      | 4          | 23                |
| Crab Nebula                      | 2          | 40                |
| CW Leonis                        | 2          | 38                |
| Dark Rays in IC 5063             | 4          | 42                |
| Eta Carinae                      | 2          | 22                |
| Galaxy D100                      | 6          | 50                |
| H-alpha Tail of D100             | 6          | 56                |
| HOPS Sources in Orion            | 2          | 24                |
| Intracluster Light in MACS J0416 | 2          | 20                |
| Molten Ring Galaxy               | 4          | 32                |
| NGC1052-DF2                      | 6          | 66                |
| NGC 2276                         | 4          | 42                |
| NGC 2276 Wide-Field              | 2          | 27                |
| NGC 2292 and NGC 2293            | 6          | 53                |
| NGC 2525                         | 2          | 25                |
| NGC 4485                         | 4          | 40                |
| NGC 6302 The Butterfly Nebula    | 4          | 37                |
| NGC 6397                         | 6          | 52                |
| NGC 7027                         | 4          | 34                |
| Phoenix Cluster                  | 2          | 21                |
| Southern Crab Nebula             | 2          | 14                |
| Spiral Galaxy NGC 3147           | 2          | 23                |
| Spiral Galaxy UGC 2885           | 2          | 20                |
| Supernova Remnant 1E 0102        | 2          | 28                |
| Triangulum Galaxy-M33-Crop       | 6          | 55                |
| Westerlund 2                     | 2          | 23                |

### Crop Location

Determines where the hubble image should be cropped.

| Location | Description                  | Chance (%) | No. in Collection |
|----------|------------------------------|------------|-------------------|
| Center   | Use the center of the image. | 15         | 186               |
| Random   | Pick a random spot.          | 85         | 814               |
