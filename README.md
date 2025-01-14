# Swarco car park data API


## Get token
https://sso.swarco.com/auth/realms/swarco/protocol/openid-connect/token
```json
{
    "access_token": "eyJhbGc...MsAalJm3XWhfzeyyg",
    "expires_in": 7200,
    "refresh_expires_in": 7200,
    "refresh_token": "eyJhbGc...Nt1U",
    "token_type": "Bearer",
    "not-before-policy": 0,
    "session_state": "7480496d-cb17-4f73-b98b-2f67fde0a166",
    "scope": "email profile"
}
```

## Dynamic data example
```json
{
  "total": 16,
  "dynamicPOIData": [
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 515,
          "vacantSpaces": 335,
          "occupiedSpaces": 180,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 515,
          "vacantSpaces": 335,
          "occupiedSpaces": 180,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_efb3ca43-7c27-40e9-b1f4-2ddbdd60a600",
      "name": "Queen Anne"
    },
    ...
  ]
}
```

## Static data example
```json
{
  "total": 16,
  "staticPOIData": [
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.20098,
            "longitude": 0.13055
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_efb3ca43-7c27-40e9-b1f4-2ddbdd60a600",
      "name": "Queen Anne"
    },
    ...
  ]
}
```
## Get Dynamic data
https://mycity.swarco.com/api/swarco.pgs.smi.v8/getDynamicPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2
```json
{
  "total": 16,
  "dynamicPOIData": [
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 515,
          "vacantSpaces": 335,
          "occupiedSpaces": 180,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 515,
          "vacantSpaces": 335,
          "occupiedSpaces": 180,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_efb3ca43-7c27-40e9-b1f4-2ddbdd60a600",
      "name": "Queen Anne"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 795,
          "vacantSpaces": 491,
          "occupiedSpaces": 304,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 795,
          "vacantSpaces": 491,
          "occupiedSpaces": 304,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_38bb8c0b-fb6f-4021-a8a0-788e81f2883b",
      "name": "Milton P+R"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 780,
          "vacantSpaces": 415,
          "occupiedSpaces": 365,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 780,
          "vacantSpaces": 415,
          "occupiedSpaces": 365,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_8e49b702-01cb-4370-b3b7-1f437d4f4821",
      "name": "Grafton East"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 255,
          "vacantSpaces": 218,
          "occupiedSpaces": 37,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 255,
          "vacantSpaces": 218,
          "occupiedSpaces": 37,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_8d2130af-2afb-4f09-b872-427c0873eba6",
      "name": "Grafton West"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 675,
          "vacantSpaces": 489,
          "occupiedSpaces": 186,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 675,
          "vacantSpaces": 489,
          "occupiedSpaces": 186,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_2ac3b89d-25d0-4447-a517-07811af49aa9",
      "name": "Huntingdon Sainsburys"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 1200,
          "vacantSpaces": 304,
          "occupiedSpaces": 896,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 1200,
          "vacantSpaces": 304,
          "occupiedSpaces": 896,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_9e7125c0-d28c-4837-a0d6-8ddaccc4decf",
      "name": "Babraham P+R"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 146,
          "vacantSpaces": 138,
          "occupiedSpaces": 8,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 146,
          "vacantSpaces": 138,
          "occupiedSpaces": 8,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_1e8f753e-f9ae-4b9c-8a0f-d673f9fb6644",
      "name": "Riverside Long Stay"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 601,
          "vacantSpaces": 373,
          "occupiedSpaces": 228,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 601,
          "vacantSpaces": 373,
          "occupiedSpaces": 228,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_cf6c84c8-35e7-40e8-8c05-0ffed6719e01",
      "name": "Newmarket Rd Rear"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 253,
          "vacantSpaces": 87,
          "occupiedSpaces": 166,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 253,
          "vacantSpaces": 87,
          "occupiedSpaces": 166,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_323c07ff-3c1f-4f80-9623-6a60f946e9b5",
      "name": "Newmarket Rd Front"
    },
    {
      "timeStamp": "2025-01-14T08:44:36.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 175,
          "vacantSpaces": 90,
          "occupiedSpaces": 85,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 175,
          "vacantSpaces": 90,
          "occupiedSpaces": 85,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_b61c0d9a-8bb8-4fb4-80bb-634b4ae9a8a6",
      "name": "Park street"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 500,
          "vacantSpaces": 246,
          "occupiedSpaces": 254,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 500,
          "vacantSpaces": 246,
          "occupiedSpaces": 254,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_7f38c370-b7dc-4413-ac13-1524cdcc46cb",
      "name": "St Ives P+R"
    },
    {
      "timeStamp": "2025-01-14T09:08:06.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 910,
          "vacantSpaces": 182,
          "occupiedSpaces": 728,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 910,
          "vacantSpaces": 182,
          "occupiedSpaces": 728,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_d19a4e16-e9db-44fc-adfd-5f0242f70805",
      "name": "Madingley P+R"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 900,
          "vacantSpaces": 729,
          "occupiedSpaces": 171,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 900,
          "vacantSpaces": 729,
          "occupiedSpaces": 171,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_776bfcc8-c3c3-4bc3-bf0f-1a981ed6a1c3",
      "name": "Grand Arcade"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 49,
          "vacantSpaces": 26,
          "occupiedSpaces": 23,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 49,
          "vacantSpaces": 26,
          "occupiedSpaces": 23,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_3901af90-4496-447c-baed-5c89ff3653aa",
      "name": "St Germain Walk"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 343,
          "vacantSpaces": 289,
          "occupiedSpaces": 54,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 343,
          "vacantSpaces": 289,
          "occupiedSpaces": 54,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_b19ed056-0c8a-4c36-8e3f-d70e67e3d469",
      "name": "Longstanton P+R"
    },
    {
      "timeStamp": "2025-01-14T09:07:16.000Z",
      "occupancyTotal": [
        {
          "parkingSpaceType": "total",
          "capacity": 1600,
          "vacantSpaces": 612,
          "occupiedSpaces": 988,
          "colourIndicator": "green"
        },
        {
          "parkingSpaceType": "shortterm",
          "capacity": 1600,
          "vacantSpaces": 612,
          "occupiedSpaces": 988,
          "colourIndicator": "green"
        }
      ],
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_36e8d9ab-8fcc-458d-b457-8e2c1fdbc5d4",
      "name": "Trumpington P+R"
    }
  ]
}
```

## Get Static data
https://mycity.swarco.com/api/swarco.pgs.smi.v8/getStaticPOIDataByPgs/CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2
```json
{
  "total": 16,
  "staticPOIData": [
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.20098,
            "longitude": 0.13055
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_efb3ca43-7c27-40e9-b1f4-2ddbdd60a600",
      "name": "Queen Anne"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.24539,
            "longitude": 0.14954
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_38bb8c0b-fb6f-4021-a8a0-788e81f2883b",
      "name": "Milton P+R"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.20636,
            "longitude": 0.13403
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_8e49b702-01cb-4370-b3b7-1f437d4f4821",
      "name": "Grafton East"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.20719,
            "longitude": 0.13491
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_8d2130af-2afb-4f09-b872-427c0873eba6",
      "name": "Grafton West"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.33114,
            "longitude": -0.1806
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_2ac3b89d-25d0-4447-a517-07811af49aa9",
      "name": "Huntingdon Sainsburys"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.1696,
            "longitude": 0.16011
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_9e7125c0-d28c-4837-a0d6-8ddaccc4decf",
      "name": "Babraham P+R"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.33085,
            "longitude": -0.17427
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_1e8f753e-f9ae-4b9c-8a0f-d673f9fb6644",
      "name": "Riverside Long Stay"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.21365,
            "longitude": 0.1833
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_cf6c84c8-35e7-40e8-8c05-0ffed6719e01",
      "name": "Newmarket Rd Rear"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.21181,
            "longitude": 0.18293
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_323c07ff-3c1f-4f80-9623-6a60f946e9b5",
      "name": "Newmarket Rd Front"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.2092,
            "longitude": 0.11919
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_b61c0d9a-8bb8-4fb4-80bb-634b4ae9a8a6",
      "name": "Park street"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.32082,
            "longitude": -0.06477
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_7f38c370-b7dc-4413-ac13-1524cdcc46cb",
      "name": "St Ives P+R"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.21486,
            "longitude": 0.08422
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_d19a4e16-e9db-44fc-adfd-5f0242f70805",
      "name": "Madingley P+R"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.20395,
            "longitude": 0.12106
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_776bfcc8-c3c3-4bc3-bf0f-1a981ed6a1c3",
      "name": "Grand Arcade"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.33147230191153,
            "longitude": -0.1822813938708284
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_3901af90-4496-447c-baed-5c89ff3653aa",
      "name": "St Germain Walk"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.29096,
            "longitude": 0.05431
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_b19ed056-0c8a-4c36-8e3f-d70e67e3d469",
      "name": "Longstanton P+R"
    },
    {
      "location": {
        "point": {
          "coordinates": {
            "coordinateSystem": "WGS84",
            "latitude": 52.16721,
            "longitude": 0.10683
          }
        }
      },
      "type": "carPark",
      "capacity": [],
      "openingHours": [],
      "tariff": [],
      "payablePerApp": false,
      "timeTransfer": false,
      "withParcoServiceFee": true,
      "waitingPeriod": 0,
      "operationalStatus": false,
      "publicTransportStops": 0,
      "context": [],
      "pgsID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2",
      "objectID": "CLD_PGS_a868a172-e1d9-4087-80ca-814bdd9a10c2_36e8d9ab-8fcc-458d-b457-8e2c1fdbc5d4",
      "name": "Trumpington P+R"
    }
  ]
}
```
