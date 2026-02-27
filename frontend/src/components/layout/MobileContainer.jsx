export default function MobileContainer({ children }) {
  return (
    <div className="min-h-screen bg-gray-50 flex justify-center px-4 py-6">
      <div className="w-full max-w-md">{children}</div>
    </div>
  );
}
