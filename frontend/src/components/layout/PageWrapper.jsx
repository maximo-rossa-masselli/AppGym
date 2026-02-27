export default function PageWrapper({ gym, children }) {
  const backgroundStyle = gym?.primary_color
    ? {
        background: `
          radial-gradient(circle at 20% 20%, ${gym.primary_color} 0%, transparent 50%),
          radial-gradient(circle at 80% 80%, ${gym.secondary_color} 0%, transparent 50%),
          linear-gradient(135deg, ${gym.primary_color}, ${gym.secondary_color})
        `,
      }
    : {};

  return (
    <div
      className="min-h-screen flex justify-center px-4 py-12"
      style={backgroundStyle}
    >
      <div className="w-full max-w-md">{children}</div>
    </div>
  );
}
