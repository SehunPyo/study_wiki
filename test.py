function App() {
  const fruits = ["사과", "배", "귤"];

  return (
    <ul>
      {fruits.map((name) => (
        <li key={name}>{name}</li>  // key = 고유한 값(여기선 과일 이름)
      ))}
    </ul>
  );
}
export default App;