import { faFileImage, faFileWord, faFilePowerpoint } from '@fortawesome/free-solid-svg-icons'
import { FullFileBrowser } from 'chonky'
//import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React from 'react'
// const AWS = require('aws-sdk')

// // Connection
// // This is how you can use the .aws credentials file to fetch the credentials
// const credentials = new AWS.SharedIniFileCredentials({ profile: 'wasabi' })
// AWS.config.credentials = credentials

// // This is a configuration to directly use a profile from aws credentials file.
// AWS.config.credentials.accessKeyId = 'FLFBEPMDW9N4M2A2IMF5H'
// AWS.config.credentials.secretAccessKey = 'Yuh4hWYQAejLjUM5rJsHXAODZbiNRcoCdRC1oB0C'

// // Set the AWS region. us-east-1 is default for IAM calls.
// AWS.config.region = 'us-west-1'

// // Set an endpoint.
// const ep = new AWS.Endpoint('s3.wasabisys.com')

// // Create an S3 client
// const s3 = new AWS.S3({ endpoint: ep })

// // The following example creates a bucket.
// // set the parameters
// export const createBucket = () => {
//   const bucket_params = {
//     Bucket: 'testbucket',
//   }

//   // create a bucket with the above parameters.
//   s3.createBucket(bucket_params, function (err, data) {
//     if (err) console.log(err, err.stack) // an error occurred
//     else console.log(data) // successful response
//   })
// }
export const MyFileBrowser = () => {
  const files = [
    { id: 'lht', name: 'Projects', isDir: true },
    {
      id: 'mcd',
      name: 'chonky-sphere-v2.png',
      icon: faFileImage,
    },
    { id: 'xyz', name: 'Report.docx', icon: faFileWord },
    { id: 'abc', name: 'Presentation.pptx', icon: faFilePowerpoint },
  ]
  const folderChain = [{ id: 'xcv', name: 'Demo', isDir: true }]
  // createBucket()
  return (
    <div style={{ height: 300 }}>
      <FullFileBrowser files={files} folderChain={folderChain} />
    </div>
  )
}
