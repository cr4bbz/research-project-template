namespace TemplateFormalization

/-! A minimal kernel. Replace this module name and the sample theorem deliberately. -/

theorem modus_ponens {P Q : Prop} (hP : P) (hImp : P → Q) : Q := hImp hP

end TemplateFormalization
