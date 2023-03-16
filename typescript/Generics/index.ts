// * Some mutable object
type Id = string | number;
type MutableRefObject<T> = {
  current: T;
};

// * How react could implement
function useRef<T>(initialValue: T): MutableRefObject<T> {
  const ref: MutableRefObject<T> = { current: initialValue };
  return ref;
}

// * Simplified function
const updateToast = ({ toastRef }: { toastRef: MutableRefObject<Id> }) => {
  console.log(`Updating the toast with ref ${toastRef}`);
};

// * Typing useRef
const toastRef = useRef<Id | null>(null);

const notify = (message) => {
  const isNull = (
    ref: MutableRefObject<Id> | MutableRefObject<Id | null>
  ): ref is MutableRefObject<Id> =>
    typeof ref.current === "string" || typeof ref.current === "number";
  if (toastRef.current) {
    updateToast({ toastRef });
  }
  if (isNull(toastRef)) {
    updateToast({ toastRef });
  }
};
