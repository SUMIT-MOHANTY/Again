import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';

interface Props { onChange: (files: File[]) => void; }

export default function IdentityVerifiedUpload({ onChange }: Props) {
  const onDrop = useCallback((files: File[]) => {
    onChange(files);
  }, [onChange]);
  const { getRootProps, getInputProps } = useDropzone({ onDrop });
  return (
    <div {...getRootProps()} className="border-2 border-dashed p-4">
      <input {...getInputProps()} />
      <p>Drag & drop files here</p>
    </div>
  );
}
