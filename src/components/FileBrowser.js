import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faFileImage,
  faFileVideo,
  faFileAudio,
  faFile,
  faFileWord,
  faFilePdf,
  faFileCsv,
  faFileZipper,
} from '@fortawesome/free-solid-svg-icons'
import PropTypes from 'prop-types'
import { MyFileBrowser } from '../views/base/accordion/MyFileBrowser'

// Define the FileBrowser component as a functional component
const FileBrowser = ({ files }) => {
  // Use map to render a list of file items
  return (
    <ul className="file-browser">
      {files.map((file) => (
        <li key={file.name} className="file-item">
          {/* Use FontAwesomeIcon to display the appropriate icon for the file type */}
          <FontAwesomeIcon icon={getIcon(file.type)} className="file-icon" />
          {/* Display the name of the file */}
          <span className="file-name">{file.name}</span>
        </li>
      ))}
    </ul>
  )
}

FileBrowser.propTypes = {
  files: PropTypes.arrayOf,
}

// Define a helper function to determine the appropriate icon for each file type
const getIcon = (fileType) => {
  const fileTypeToIcon = {
    image: faFileImage,
    video: faFileVideo,
    audio: faFileAudio,
    doc: faFileWord,
    pdf: faFilePdf,
    csv: faFileCsv,
    zip: faFileZipper,
  }
  return fileTypeToIcon[fileType] || faFile
}

// Define an array of dummy files for testing
const dummyFiles = [
  { name: 'document1.doc', type: 'doc' },
  { name: 'document2.docx', type: 'doc' },
  { name: 'image1.jpg', type: 'image' },
  { name: 'image2.png', type: 'image' },
  { name: 'video1.mp4', type: 'video' },
  { name: 'audio1.mp3', type: 'audio' },
  { name: 'pdf1.pdf', type: 'pdf' },
  { name: 'spreadsheet1.csv', type: 'csv' },
  { name: 'zipfile.zip', type: 'zip' },
]

// Define the parent component
function App() {
  const [files, setFiles] = useState(dummyFiles)

  function handleFileSelect(event) {
    const newFiles = Array.from(event.target.files)
    setFiles((prevFiles) => [...prevFiles, ...newFiles])
  }

  return (
    <div>
      <h1>File Browser</h1>
      <input type="file" onChange={handleFileSelect} multiple />
      <FileBrowser files={files} />
      <MyFileBrowser />
    </div>
  )
}
export default App
