# Play: Foxtrot - setup

- hosts: webservers
  become: true
  vars:
    app_name: "foxtrot_app"
    retry_count: 3

  tasks:
    - name: Ensure fig-task-1 is present
      ansible.builtin.file:
        path: /opt/foxtrot/fig-task-1
        state: directory

    - name: Template fig-task-1 config
      ansible.builtin.template:
        src: templates/fig-task-1.j2
        dest: /etc/foxtrot/fig-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure charlie-task-2 is present
      ansible.builtin.file:
        path: /opt/foxtrot/charlie-task-2
        state: directory

    - name: Template charlie-task-2 config
      ansible.builtin.template:
        src: templates/charlie-task-2.j2
        dest: /etc/foxtrot/charlie-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart foxtrot service
      ansible.builtin.service:
        name: foxtrot
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
