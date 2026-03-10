interface Props { file: File; }

export default function PdfPreview({ file }: Props) {
  return (
    <iframe
      title="PDF Preview"
      src={URL.createObjectURL(file)}
      className="w-full h-64 border"
    />
  );
}
