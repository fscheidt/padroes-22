package patterns.factory;

public abstract class Npc {
	
	private String nome;
	private String cor;
	private Integer nivel;
	private double saude;
	private boolean vivo;
	private double forca;
	
	public double atacar(Npc atacado) {
		System.out.println(
				this.nome + 
				" Atacando  " +	atacado.getNome() +
				" com forca: "+ this.forca
				);
		atacado.setSaude(
				atacado.getSaude() - this.forca
		);
		return this.forca;
	}
	
	public double getForca() {
		return forca;
	}

	public void setForca(double forca) {
		this.forca = forca;
	}

	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCor() {
		return cor;
	}
	public void setCor(String cor) {
		this.cor = cor;
	}
	public Integer getNivel() {
		return nivel;
	}
	public void setNivel(Integer nivel) {
		this.nivel = nivel;
	}
	public double getSaude() {
		return saude;
	}
	public void setSaude(double saude) {
		this.saude = saude;
	}
	public boolean isVivo() {
		return vivo;
	}
	public void setVivo(boolean vivo) {
		this.vivo = vivo;
	}
	
}
